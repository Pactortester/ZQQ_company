# -*- coding: utf-8 -*-
# @Time    : 2019/1/8 18:42
# @Author  : lijiawei
# @Email   : lijiawei@quandashi.com
# @FileName: logincookie.py
# @Software: PyCharm
# @Blog    : https://blog.csdn.net/flower_drop

import time


class LoginPage:

    url = "https://www.zhiqianqiu.com/"

    cookie = ({'value': 's%3AVwneJ-UEOj0eeRNuSOUsn7P10ozkVrIq.6oPjCm4XgEuwEvwScDqXZacnCyTTmRi0AgPEtJ2UAl4',
               'expiry': 1862620474.690297,
               'domain': 'www.zhiqianqiu.com',
               # 'httpOnly': True,
               'name': 'connect.sid',
               # 'secure': False,
               'path': '/'})

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.url)

    def login(self):
        self.open_page()
        self.driver.add_cookie(self.cookie)
        self.driver.refresh()
        time.sleep(1)

    def refresh(self):
        self.driver.add_cookie(self.cookie)
        self.driver.refresh()
        time.sleep(1)