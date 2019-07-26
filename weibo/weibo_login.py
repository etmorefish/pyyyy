# -*- coding: utf-8 -*-
# @Time    : 19-6-21 下午8:57
# @Author  : MaoLei
# @Email   : maolei025@qq.com
# @File    : weibo_login.py
# @Software: PyCharm
import binascii
import re
import time
import json
import requests
import base64

from urllib import parse
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5


def get_username(username):
    res = parse.quote(username)
    res = base64.b64encode(res.encode())
    return res.decode('utf-8')


def get_password(password ,pubkey):
    publickey = RSA.RsaKey(n=int(pubkey, 16), e=65537)
    cipher = PKCS1_v1_5.new(publickey)
    res = cipher.encrypt(password.encode())
    return binascii.b2a_hex(res).decode()

session = requests.session()

session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'
})

# 1.请求首页面
# session.get('https://weibo.com')

# 2.请求pre_login 获取参数
params = {
            'entry': 'weibo',
            'callback': 'sinaSSOController.preloginCallBack',
            'su': '',
            'rsakt': 'mod',
            'client': 'ssologin.js(v1.4.19)',
            '_': int(time.time())
        }
res = session.get(url='https://login.sina.com.cn/sso/prelogin.php', params=params)
data = json.loads(re.findall(r'\((.*?)\)', res.text)[0])
print(data)
t2 = str(int(time.time()*1000))


form_data = {
    'entry': 'weibo',
    'gateway': '1',
    'from': '',
    'savestate': '7',
    'qrcode_flag': 'false',
    'useticket': '1',
    'pagerefer': '',
    'vsnf': 1,
    'su': get_username('m13409639216@163.com'),
    'service': 'miniblog',
    'servertime': data['servertime'],
    'nonce': data['nonce'],
    'pwencode': 'rsa2',
    'rsakv': data['rsakv'],
    'sp': get_password( str(data['servertime']) + '\t' + data['nonce']+'\n'+'849078367',data['pubkey']),
    'sr': '1920*1080',
    'encoding': 'UTF-8',
    'prelt': '49',
    'url': 'https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',
    'returntype': 'META'
}
# 校验用户名和密码
print(form_data)
login_url = 'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)'
res = session.post(url=login_url, data=form_data)
res.encoding = 'gbk'
# print(res.text)
redirect_url = re.findall(r'replace\("(.*?)"\)',res.text)[0]

res = session.get(url=redirect_url)
res.encoding = 'gbk'
print(res.text)
arrurls = re.findall(r'"arrURL":(\[.*?\])',res.text)[0]
arrurls = json.loads(arrurls)
res1 = session.get(arrurls[0])
print(res1.text)
print('-'*100)
home_res = session.get('https://weibo.com/?wvr=5&lf=reg')
print(home_res.text)