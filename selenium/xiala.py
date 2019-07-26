# -*- coding: utf-8 -*-
# @Time    : 19-6-28 下午4:41
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : xiala.py
# @Software: PyCharm


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


# 打开谷歌浏览器
driver = webdriver.Chrome()
# 访问页面
driver.get('https://v3.bootcss.com/css/#%E4%B8%8B%E6%8B%89%E5%88%97%E8%A1%A8%EF%BC%88select%EF%BC%89')
# 获取属性name='q'的元素
element = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[6]/div[20]/form/select')
# 清空它的text值，如果它是一个可以输入text的元素
# all_options = select.find_elements_by_tag_name('option')
#
# for option in all_options:
#     print('Text is: %s;Value is :%s'%(option.text,option.get_attribute('value')))
#
# for option in all_options:
#     if option.text == '2':
#         option.click()

select = Select(element)

# select.select_by_index(2)
# time.sleep(3)
# select.select_by_visible_text('4')
# time.sleep(3)
# select.deselect_by_value('2')
# time.sleep(2)
# select.deselect_all()

options = select.options
for i in range(len(options-1)):
    if i%2:
        options[i].click()
time.sleep(3)
select.deselect_all()










