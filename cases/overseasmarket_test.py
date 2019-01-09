# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 16:53
# @Author  : lijiawei
# @Email   : lijiawei@quandashi.com
# @FileName: overseasmarket_test.py
# @Software: PyCharm
# @Blog    : https://blog.csdn.net/flower_drop
from base.TrademarkBusiness import BasePage
from utils.mytestcase import MyTestCase


class OverseasMarket(MyTestCase):
    """海外市场"""

    def test_md(self):
        """马德里商标注册"""
        xm = BasePage(self.driver)
        xm.trade_name("马德里商标注册", "马德里商标注册_专注于商标查询、专利查询-知千秋官网", "test_md.png")

    def test_mg(self):
        """美国商标注册"""
        xm = BasePage(self.driver)
        xm.trade_name("美国商标注册", "美国商标注册_专注于商标查询、专利查询-知千秋官网", "test_mg.png")
