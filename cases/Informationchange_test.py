# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 16:39
# @Author  : lijiawei
# @Email   : lijiawei@quandashi.com
# @FileName: Informationchange_test.py
# @Software: PyCharm
# @Blog    : https://blog.csdn.net/flower_drop
from base.TrademarkBusiness import BasePage
from utils.mytestcase import MyTestCase


class InformationChange(MyTestCase):
    """信息变更"""

    def test_bg(self):
        """商标变更"""
        xm = BasePage(self.driver)
        xm.trade_name("商标变更", "商标变更_专注于商标查询、专利查询-知千秋官网", "test_bg.png")

    def test_xz(self):
        """商标续展"""
        xm = BasePage(self.driver)
        xm.trade_name("商标续展", "商标续展_专注于商标查询、专利查询-知千秋官网", "test_xz.png")

    def test_ba(self):
        """商标许可备案"""
        xm = BasePage(self.driver)
        xm.trade_name("商标许可备案", "商标许可备案_专注于商标查询、专利查询-知千秋官网", "test_ba.png")

    def test_zx(self):
        """商标注销"""
        xm = BasePage(self.driver)
        xm.trade_name("商标注销", "商标注销_专注于商标查询、专利查询-知千秋官网", "test_zx.png")

    def test_zr(self):
        """商标转让"""
        xm = BasePage(self.driver)
        xm.trade_name("商标转让", "商标转让_专注于商标查询、专利查询-知千秋官网", "test_zr.png")

    def test_bf(self):
        """补发商标注册证申请"""
        xm = BasePage(self.driver)
        xm.trade_name("补发商标注册证申请", "补发商标注册证申请_专注于商标查询、专利查询-知千秋官网", "test_bf.png")

    def test_cj(self):
        """出具商标注册证明申请"""
        xm = BasePage(self.driver)
        xm.trade_name("出具商标注册证明申请", "出具商标注册证明申请_专注于商标查询、专利查询-知千秋官网", "test_cj.png")

    def test_gz(self):
        """商标更正"""
        xm = BasePage(self.driver)
        xm.trade_name("商标更正", "商标更正_专注于商标查询、专利查询-知千秋官网", "test_gz.png")