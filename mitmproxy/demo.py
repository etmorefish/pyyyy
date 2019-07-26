# -*- coding: utf-8 -*-
# @Time    : 19-7-24 下午4:55
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : demo.py
# @Software: PyCharm


from selenium import  webdriver
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://127.0.0.1:8080")
dirver = webdriver.Chrome(chrome_options=options)