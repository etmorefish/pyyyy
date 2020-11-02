import requests

# 配置区
SendKey = ''
title = '哈哈哈'
desp = '感觉提醒还可以，反馈比较明显声音'
openid = 'otA3G5wfU62_RYwyOuJPDOCmMIoA'
# 配置区
url = 'https://sctapi.ftqq.com/SCT1925TWhOheHFauroldfGd37PhsYOD' +'.send'
data = {'title': title,
        'desp': desp,
        'openid': openid}
req = requests.post(url, data).text
print(req)
