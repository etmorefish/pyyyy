import csv
import requests
from lxml import etree

url = 'http://top.baidu.com/?fr=mhd_card'

res = requests.get(url=url)
res.encoding = res.apparent_encoding

html = etree.HTML(res.text)

titles = html.xpath("//ul[@id='hot-list']/li/a[1]/@title")
links = html.xpath("//ul[@id='hot-list']/li/a[1]/@href")

# print(title, link)
with open('baidu_hot.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['title', 'link'])
    for i in range(len(titles)):
        writer.writerow([titles[i], links[i]])
