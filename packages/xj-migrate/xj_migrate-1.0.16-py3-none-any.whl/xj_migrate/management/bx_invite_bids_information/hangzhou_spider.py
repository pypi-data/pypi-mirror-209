# encoding: utf-8
"""
@project: djangoModel->hangzhou_spider
@author: 孙楷炎
@Email: sky4834@163.com
@synopsis: 杭州市的爬取文件
@created_time: 2023/5/4 12:15
"""
from config.config import JConfig
from xj_migrate.utils.custom_tool import write_to_log
from ..spider_base import SpiderBase

main_config = JConfig()


class HanZhouSpider(SpiderBase):
    key = "HangZhou"  # 该爬虫类的搜索key
    url = "https://ggzy.hzctc.hangzhou.gov.cn/SecondPage/SecondPage?ModuleID=67&ViewID=17"  # 爬取的入口链接地址
    save_path = ""  # 保存的文件地址
    heartbeat = -1  # 爬取的频率是否需要定时暂定频率，单位为秒

    def __init__(self):
        self.save_path = main_config.get_base_dir("pass")

    def get_link(self):
        """
        如果是需要再二级页面获取信息则需要进行先获取链接点击
        :return:
        """
        pass

    def node_select(self):
        """
        节点选择,xpath,ID,Class等等
        必须继承并且重写该方法
        :return:
        """
        pass

    def run(self):
        """
        执行爬虫的方法，其他自定义获取
        必须继承并且重写该方法
        :return:
        """
        write_to_log(prefix="打印日志系統叫脚本", content=self.save_path)
        return self.save_path

    def save(self):
        """
        将爬取的文件保存到excel或者csv文件里面
        统一使用数据库迁移迁移导入数据库
        :return:
        """
        pass
