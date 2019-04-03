# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 10:16
# @Author  : lijiawei
# @Email   : lijiawei@quandashi.com
# @FileName: legalservice_test.py
# @Software: PyCharm
# @Blog    : https://blog.csdn.net/flower_drop
import time

from utils.mytestcase import MyTestCase
from base.TrademarkBusiness import BasePage


class LegalService(MyTestCase):
    """法律服务"""

    def test_bh(self):
        """商标驳回复审"""
        xm = BasePage(self.driver)
        xm.trade_name("商标驳回复审", "商标驳回复审_专注于商标查询、专利查询-知千秋官网", "test_bh.png")

    def test_cs(self):
        """商标撤三申请"""
        xm = BasePage(self.driver)
        xm.trade_name("商标撤三申请", "商标撤三申请_专注于商标查询、专利查询-知千秋官网", "test_cs.png")

    def test_cd(self):
        """商标撤三答辩"""
        xm = BasePage(self.driver)
        xm.trade_name("商标撤三答辩", "商标撤三答辩_专注于商标查询、专利查询-知千秋官网", "test_cd.png")

    def test_ys(self):
        """商标异议申请"""
        xm = BasePage(self.driver)
        xm.trade_name("商标异议申请", "商标异议申请_专注于商标查询、专利查询-知千秋官网", "test_ys.png")

    def test_yb(self):
        """商标异议答辩"""
        xm = BasePage(self.driver)
        xm.trade_name("商标异议答辩", "商标异议答辩_专注于商标查询、专利查询-知千秋官网", "test_yb.png")

    def test_wx(self):
        """商标无效宣告"""
        xm = BasePage(self.driver)
        xm.trade_name("商标无效宣告", "商标无效宣告申请_专注于商标查询、专利查询-知千秋官网", "test_wx.png")





