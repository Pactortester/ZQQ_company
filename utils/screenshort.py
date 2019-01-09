# -*- coding: utf-8 -*-
# @Time    : 2019/1/9 9:57
# @Author  : lijiawei
# @Email   : lijiawei@quandashi.com
# @FileName: screenshort.py
# @Software: PyCharm
# @Blog    : https://blog.csdn.net/flower_drop

import time

from config.globalparam import img_path


def get_screenshort(driver, file_name):
    time_c = time.strftime("%Y-%m-%d_%H-%M-%S_")
    path = img_path + '\\'+time_c+file_name
    time.sleep(1)
    driver.get_screenshot_as_file(path)
