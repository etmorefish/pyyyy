# -*- coding: utf-8 -*-
# @Time    : 19-11-17 下午7:42
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : test1.py
# @Software: PyCharm

import time
from  selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.prettylittlething.com/sale/view-all-sale.html?navigation-sale-viewall')
time.sleep(5)
print(driver.page_source)