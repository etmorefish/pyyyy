# -*- coding: utf-8 -*-
# @Time    : 20-4-11 下午11:07
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : wuyuan.py
# @Software: PyCharm
import re
import time
import  requests
from lxml import etree
url = 'http://59.172.226.5:80/eams/sso/login.action?targetUrl={base64}aHR0cDovLzU5LjE3Mi4yMjYuNTo4MC9lYW1zL2hvbWUuYWN0aW9u'
url1 = 'http://uia.whxy.edu.cn/cas/login?service=http%3A%2F%2F59.172.226.5%3A80%2Feams%2Fsso%2Flogin.action%3FtargetUrl%3D%7Bbase64%7DaHR0cDovLzU5LjE3Mi4yMjYuNTo4MC9lYW1zL2hvbWUuYWN0aW9u'
session = requests.session()
session.headers.update({
    "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
})
# session.get(url='http://uia.whxy.edu.cn/cas/signout/logoutFull?service=http://59.172.226.5:80/eams/login.action')
time.sleep(3)

res = session.get(url=url)
lt = re.findall(r'name="lt" value="(.*)"',res.text)[0]
# print(lt)

params = {
    "username": 16202050539,  # 改成你自己的
    "password": 6666666,  # 改成你自己的
    "lt": lt,
    "_eventId": "submit"
}
time.sleep(3)
res = session.post(url=url1, data=params)
# print('-'*50,res.text)
time.sleep(1)

url3 = 'http://59.172.226.5/eams/home.action'
res = session.get(url = url3)
r = etree.HTML(res.text)
user = r.xpath("//form[@id='form11754836551']/a[9]/text()")[0]
if user:
    print('登录成功-',user)
# print('登录成功','*'*50,res.text)
'''
http://uia.whxy.edu.cn/cas/login?service=http%3A%2F%2F59.172.226.5%3A80%2Feams%2Fsso%2Flogin.action%3FtargetUrl%3D%7Bbase64%7DaHR0cDovLzU5LjE3Mi4yMjYuNTo4MC9lYW1zL2hvbWUuYWN0aW9u
username: 16202050538
password: 666666
lt: _cEF7830EA-3EFB-4783-D9E5-8D282DD48B70_kAE384655-DDAB-F71E-8016-2E14FE06D705
_eventId: submit
http://uia.whxy.edu.cn/cas/login?service=http%3A%2F%2F59.172.226.5%3A80%2Feams%2Fsso%2Flogin.action%3FtargetUrl%3D%7Bbase64%7DaHR0cDovLzU5LjE3Mi4yMjYuNTo4MC9lYW1zL2hvbWUuYWN0aW9u

'''