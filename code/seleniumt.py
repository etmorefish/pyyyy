#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date    : 2019-01-10 16:23:17
# @Author  : lilei (849078367@qq.com)
# @Link    : https://zhuanlan.zhihu.com/p/31127896
# @Version : $Id$


from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

caps = webdriver.DesiredCapabilities().FIREFOX
caps["marionette"] = True
binary = FirefoxBinary(r'/opt/firefox/firefox')
#把上述地址改成你电脑中Firefox程序的地址
driver = webdriver.Firefox(firefox_binary=binary, capabilities=caps)
driver.get("http://www.santostang.com/2018/07/04/hello-world/")

driver.switch_to.frame(driver.find_element_by_css_selector("iframe[title='livere']"))


comments = driver.find_elements_by_css_selector('div.reply-content')
for eachcomment in comments:
    content = eachcomment.find_element_by_tag_name('p')
    print (content.text)