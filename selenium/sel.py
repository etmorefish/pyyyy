# -*- coding: utf-8 -*-
# @Time    : 19-6-27 下午8:58
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : sel.py
# @Software: PyCharm

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
# print(driver.title)

# 打开谷歌浏览器
driver = webdriver.Chrome()
# 访问页面
driver.get('http://www.baidu.com')
# 获取属性name='q'的元素
elem = driver.find_element_by_name('wd')
# 清空它的text值，如果它是一个可以输入text的元素
elem.clear()
# 模拟输入'pycon'
elem.send_keys('pycon')
# 模拟回车键进行搜索
elem.send_keys(Keys.ENTER)
# 关闭浏览器
time.sleep(5)
driver.close()