# encoding: utf-8
"""
@project: djangoModel->synchronous_mysql_synchronous
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 使用pandas，数据库同步脚本
@created_time: 2023/5/18 17:47
"""
import os
import time

from django.core.management.base import BaseCommand, no_translations
from pandas import DataFrame
import pandas as pd
import pymysql
import sqlalchemy
from sqlalchemy import create_engine

from config.config import JConfig
from xj_migrate.utils.custom_tool import format_params_handle, write_to_log, force_transform_type


# 自定义异常类，记录异常，并打印错误信息
class MigrateError(Exception):
    def __init__(self, err_msg=None, *args, catch_err=None, **kwargs):
        super().__init__(self)
        self.err_msg = err_msg or str(catch_err)
        self.catch_err = catch_err

    def __str__(self):
        if self.catch_err:
            write_to_log(prefix="迁移异常", err_obj=self.catch_err)
        else:
            write_to_log(prefix="迁移异常", content=self.err_msg)
        err_msg = self.err_msg or str(self.catch_err)
        return err_msg


class Command(BaseCommand):
    # note 注意不同结构的表进行同步时候，需要设计好迁移的表的执行顺序、字段映射、迁移表映射。还有外键冲突，
    # 报错 TypeError: __init__() got multiple values for argument 'schema' ===>>> 处理方案： 更新依赖包：sqlalchemy==1.4.46，pandas==1.3.5
    # 报错：sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (1054, "Unknown column 'index' in 'field list'") ===>>> 处理：index=False

    help = "同步数据库中配置表的结构和数据"
    from_engine = None  # 迁移源数据库配置
    to_engines = []  # 被迁移的数据配置
    migrate_mapping = {}  # 迁移的表映射
    append_table_id_mapping = {}  # 追加模式的时候字段冲突，主键ID映射。其他关联的表获自行获取修改关联ID。

    def add_arguments(self, parser):
        parser.add_argument('--if_exists',
                            dest='if_exists',
                            default="replace",
                            help='迁移数据库，采用追加模式还是替换模式')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config = JConfig()

        # 数据库连接相关
        self.from_engine = None
        self.to_engines = []
        self.from_db_map = self.config.get_list_by_cut(
            section="xj_migrate",
            option="migrate_from_db",
            map_key_list=["host", "user", "password", "database", "port"],
            cut_char=","
        )
        self.migrate_to_dbs = self.config.parse_lines_tuple(
            section="xj_migrate",
            option="migrate_to_dbs",
            cut_char=",",
            map_key_list=["host", "user", "password", "database", "port"]
        )

        # 迁移配置相关,结构如下
        # {
        #   "flow_flow": { 迁移的原表
        #     "table_mapping": "flow_flow2", 目标表明
        #     "fields_mapping": {
        #       "module_name": "module_name2" 表字段不一致，建立映射
        #     },
        #     "primary_key": "id", 声明主键，因为替换模式会替换掉主键ID，所以需要重新声明
        #     "need_backup": true, 是否需要备份，目前强制备份
        #     "relate_other_table_key": [], # 该表关联的外键有那些
        #     "remove_fields": [ 移除掉不需要迁移的字段
        #       "id"
        #     ]
        #   }
        # }
        self.migrate_mapping = self.config.load_json_configure("migrate_mapping.json")
        self.migrate_tables = self.config.get_list_by_cut(section="xj_migrate", option="migrate_tables", cut_char=",")

    @staticmethod
    def create_connect(config_dict: dict = None, use_sqlalchemy: bool = True, **kwargs):
        """
        构建数据库连接
        :param config_dict: 数据库参数
        :param use_sqlalchemy: 是否使用sqlalchemy引擎
        :return: data,err
        """
        # ================== section 获取基础参数 start ===============================
        config_dict, is_pass = force_transform_type(variable=config_dict, var_type="only_dict", default={})
        kwargs, is_pass = force_transform_type(variable=kwargs, var_type="only_dict", default={})
        config_dict.update(kwargs)
        host = config_dict.get("host", None)
        user = config_dict.get("user", None)
        password = config_dict.get("password", None)
        database = config_dict.get("database", None)
        port, is_pass = force_transform_type(variable=config_dict.get("port", None), var_type="int")
        use_sqlalchemy, is_pass = force_transform_type(variable=use_sqlalchemy, var_type="bool", default=False)
        if not host or not user or not password or not port:
            return None, "参数错误"
        # ================== section 获取基础参数 end ===============================
        try:
            # 使用sqlalchemy引擎
            if use_sqlalchemy:
                # 注意由于pandas兼容问题，写入的时候需要使用
                mysql_client_str = 'mysql+pymysql://' + str(user) + ':' + str(password) + '@' + str(host) + ':' + str(port) + '/' + str(database)
                return create_engine(mysql_client_str), None
            else:
                # 直接使用pymysql
                config_dict["port"], is_pass = force_transform_type(variable=config_dict.get("port", 3306), var_type="int", default=3306)
                return pymysql.connect(host=host, user=user, password=password, database=database, port=port), None
        except Exception as e:
            return None, str(e)

    @staticmethod
    def table_fields_types(engine, table_name: str = None):
        table = sqlalchemy.Table(table_name, sqlalchemy.MetaData(), autoload=True, autoload_with=engine)
        return {k: v.type for k, v in table.c.items()}

    def data_backup(self, pf, table_name="", save_type="to_json"):
        """在同步之前，把目标表做一次备份"""
        if not save_type in save_type:
            return False, "不是有效的保存方式"
        today = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        save_path = self.config.get_base_dir() + "/resource_files/backup_files/" + today + '/'
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        save_name = table_name + "-" + today + "-backup"
        save_path = save_path + save_name
        if save_type == "to_json":
            pf.to_json(save_path + ".json")
        elif save_type == "to_csv":
            pf.to_csv(save_path + ".csv")
        elif save_type == "to_excel":
            pf.to_excel(save_path + ".xlsx")

    @staticmethod
    def replace_insert(df: DataFrame, migrate_table, to_engine, fields_mapping, primary_key="id", **kwargs):
        """替换默认插入"""
        df.to_sql(
            name=migrate_table,
            con=to_engine,
            if_exists="replace",
            dtype=fields_mapping,
            index=False
        )
        # note 替换模式会覆盖掉原有的主键ID，所以需要重新加回来。 暂时pandas还没有更好的解决办法
        con = to_engine.connect()
        con.execute("""ALTER TABLE `{}` 
        MODIFY COLUMN `{}` bigint(20) NOT NULL AUTO_INCREMENT FIRST,
        ADD PRIMARY KEY (`{}`);""".format(migrate_table, primary_key, primary_key))

    def append_insert(self, df: DataFrame, migrate_table, to_engine, fields_mapping, primary_key="id", **kwargs):
        """追加模式插入"""
        # TODO 保存之前处理外键关联的问题，所以设计好导入的顺序。先导入的结果营销后面的结果
        df.to_sql(
            name=migrate_table,
            con=to_engine,
            if_exists="append",
            dtype=fields_mapping,
            index=False,
            method=self.append_insert_callback
        )

    def append_insert_callback(self, table, conn, keys, data_iter):
        """
        Pandas中to_sql方法的回调函数
        :param table:Pandas的table
        :param conn:数据库驱动连接对象
        :param keys:要存入的字段名
        :param data_iter:DataFrame对象也就是数据迭代器
        :return:
        """
        # TODO 需要完成，追加模式。完成主键冲突，去除主键自动添加，并且相关联的表自动更新管理的值
        dbapi_conn = conn.connection
        # 创建数据库游标对象
        with dbapi_conn.cursor() as cursor:
            # 遍历拼接sql语句
            for data_tuple in data_iter:
                sql = """INSERT INTO {TABLE_NAME}(bill_name, room_number, bind_status, community_name, area_m) VALUES('{BILL_NAME}', '{ROOM_NUMBER}', {BIND_STATUS}, '{COMMUNITY_NAME}', {AREA_M}) ON conflict({UNIQUE_LIST}) DO UPDATE SET bill_name='{BILL_NAME}', bind_status={BIND_STATUS}, area_m='{AREA_M}'""".format(
                    TABLE_NAME=table.name, UNIQUE_LIST="community_name, room_number",
                    BILL_NAME=data_tuple[0], ROOM_NUMBER=data_tuple[2], COMMUNITY_NAME=data_tuple[1],
                    BIND_STATUS=data_tuple[3], AREA_M=data_tuple[4])
                cursor.execute(sql)

    @no_translations
    def handle(self, *args, **options):
        # note 业务逻辑入口
        input_if_exists = options.get("if_exists", "replace")
        input_if_exists = input_if_exists if input_if_exists in ["replace", "append"] else "replace"
        if not self.migrate_tables:
            raise MigrateError("没有找到需要迁移的表")
        # ============ section 创建mysql操作对象 start===================
        # 来源数据库创建连接
        self.from_engine, err = self.create_connect(self.from_db_map, use_create_engine=True)
        if err:
            raise MigrateError("无法连接迁移源")
        # 同步的数据库创建连接
        for i in self.migrate_to_dbs:
            conn, err = self.create_connect(i, use_create_engine=True)
            if err:
                raise MigrateError("无法连接目标源")
            self.to_engines.append(conn)
        # ============ section 创建mysql操作对象 end  ===================

        for table_name in self.migrate_tables:
            # ============ section 获取源数据 start ===================
            df = pd.read_sql("SELECT * FROM `" + table_name + "`", self.from_engine)
            from_table_fields = self.table_fields_types(engine=self.from_engine, table_name=table_name)
            # ============ section 获取源数据 end   ===================

            for to_engine in self.to_engines:
                # ============ section 进行表迁移映射，以及进行表字段映射 ===================
                # A库的a表迁移到B库的b表。然后a表字段field1，迁移到b表后字段变成fields2
                migrate_table = self.migrate_mapping.get(table_name, {}).get("table_mapping", table_name)
                fields_mapping = format_params_handle(
                    param_dict=self.migrate_mapping.get(table_name, {}).get("fields_mapping", {}),
                    filter_filed_list=df.columns.to_list()
                )
                if fields_mapping:
                    from_table_fields = format_params_handle(param_dict=from_table_fields, alias_dict=fields_mapping)
                    df = df.rename(columns=format_params_handle(
                        param_dict=fields_mapping,
                        filter_filed_list=df.columns.to_list(),
                    ))
                # ============ section 进行表迁移映射，以及进行表字段映射 ===================

                # ============ section 迁移之前先对目标表数据进行备份 start ===================
                try:
                    copy_df = pd.read_sql("SELECT * FROM `" + migrate_table + "`", to_engine)
                    self.data_backup(copy_df, table_name=migrate_table)
                except sqlalchemy.exc.ProgrammingError:
                    pass
                except Exception as e:
                    raise MigrateError(catch_err=e)
                # ============ section 迁移之前先对目标表数据进行备份 end   ===================

                # note 开始迁移
                if input_if_exists == "replace":
                    self.replace_insert(df, migrate_table, to_engine, from_table_fields)
                else:
                    self.append_insert(df, migrate_table, to_engine, from_table_fields)
