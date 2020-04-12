import requests
import pandas as pd
from pandas import DataFrame
flag = [1,2,3,4,5,6,7,8,9,10]
urllist = []
for i in flag:
    url = f"https://itunes.apple.com/rss/customerreviews/page={i}/id=930368978/sortby=mostrecent/json?l=en&&cc=cn"
    urllist.append(url)
rating = [] #评分
title = [] #标题
content = [] #内容
for url in urllist:
    res = requests.get(url)
    data = res.json()['feed']['entry']
    for i in range(len(data)):
        rating.append(data[i]['im:rating']['label'])
        title.append(data[i]['title']['label'])
        content.append(data[i]['content']['label'])
data = {'打分':rating,
       '标题':title,
       '内容':content
       }
df = DataFrame(data)
# print(df)
# r = df[df['标题'].str.contains['好评']]
# print(r)
df.to_csv('result.csv', index=True, header=True)