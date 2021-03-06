# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 9:49
# @Author  : lijiawei
# @Email   : lijiawei@quandashi.com
# @FileName: mytestcase.py
# @Software: PyCharm
# @Blog    : https://blog.csdn.net/flower_drop

# coding=utf-8
import os
import unittest
import time
from config.globalparam import driver_path
from utils.log import Log
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.pyselenium import logger


class MyTestCase(unittest.TestCase):
    """
    The base class is for all test cases. This is a father .
    """
    success = "SUCCESS   "
    fail = "FAIL   "
    logger = Log()

    def setUp(self):
        self.logger = Log()
        self.logger.info('############################### START ###############################')
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # self.driver = webdriver.Chrome(options=chrome_options, executable_path=driver_path + "\\" + "chromedriver.exe")
        self.driver = webdriver.Chrome(driver_path + "\\" + "chromedriver.exe")
        self.driver.maximize_window()
        self.driver.set_window_size(1920,1080)
        self.driver.implicitly_wait(30)

    def tearDown(self):
        time.sleep(2)
        # self.driver.quit()
        self.logger.info('###############################  END  ###############################')

    @staticmethod
    def my_print(msg):
        logger.info(msg)
