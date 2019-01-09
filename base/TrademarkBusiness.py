# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 13:49
# @Author  : lijiawei
# @Email   : lijiawei@quandashi.com
# @FileName: TrademarkBusiness.py
# @Software: PyCharm
# @Blog    : https://blog.csdn.net/flower_drop
import time
import unittest

from selenium.webdriver import ActionChains
from utils.randomdata import unicode
from utils.logincookie import LoginPage
from utils.mytestcase import MyTestCase
from utils.screenshort import get_screenshort


class BasePage(MyTestCase):

    def __init__(self, driver):
        self.driver = driver
        unittest.TestCase.__init__(self)

    def trade_name(self, name, title, images):
        dl = LoginPage(self.driver)
        dl.login()
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "#__layout > div > div:nth-child(1) > div:nth-child(1) > div > div.fl.drop_nav")).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_css_selector(
            "#__layout > div > div:nth-child(1) > div:nth-child(1) > div > div.hoverMenu.drop-body > ul.cont.cont-1 > li > h3 > a")).perform()
        ActionChains(self.driver).release()
        self.driver.find_element_by_link_text(name).click()
        time.sleep(3)
        # 获取打开的多个窗口句柄
        windows = self.driver.window_handles
        # 切换到当前最新打开的窗口
        self.driver.switch_to.window(windows[-1])
        time.sleep(2)
        self.driver.set_window_size(1920, 1080)
        self.assertEqual(title, self.driver.title)
        print(self.driver.title)

        price_text_1 = str(self.driver.find_element_by_css_selector(
            "#__layout > div > div.show-content > div.w1200 > div.product > div.hidden > div.type > dl:nth-child(3) > dd > b").text).replace(
            "¥", "")
        s1 = int(price_text_1) + 0
        print("总费用:" + price_text_1)

        self.driver.find_element_by_link_text("立即办理").click()

        self.driver.find_element_by_name("name").send_keys(unicode())
        self.driver.find_element_by_name("phone").send_keys("18636825212")
        self.driver.find_element_by_name("email").send_keys("test@zhiqianqiu.com")
        self.driver.find_element_by_class_name("myTextarea").send_keys(time.strftime("%Y-%m-%d_%H-%M-%S") + "测试订单")
        get_screenshort(self.driver, images)
        price_text_2 = self.driver.find_element_by_css_selector(
            "#__layout > div > div.content.myOrder-wrap.w1200 > div > div:nth-child(6) > div.last-pay.personal-last-pay > ul > li.row-sense > em > i").text
        s2 = int(price_text_2) + 0
        self.assertEqual(s1, s2, "金额异常!")

        self.driver.find_element_by_link_text("提交订单").click()

        info = self.driver.find_element_by_css_selector(
            "#__layout > div > div.smartRegister-page.smartRegister3-page > div.paying-wrap > div.section-orderInfo.clearfix > div > div").text

        print(str(info))

        price_text_3 = str(self.driver.find_element_by_class_name("payable").text).replace("￥", "").replace(".00", "")
        s3 = int(price_text_3) + 0

        self.assertEqual(s2, s3, "金额异常!")
        print("价格一致!")
        self.driver.find_element_by_link_text("确认支付").click()
        print(name + "测试通过!")


