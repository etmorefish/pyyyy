import requests as req  # 导入第三方开源包 requests,并将报名重新定义为req

'''
1.获取用户输入，并检查用户输入
2.找到输入歌曲的所关联的url片段
3.根据请求得到的响应体，分析响应体并找到歌曲信息，并关联url，伪造请求
4.分析歌曲信息url，找到关联歌名的一些特征信息
5.在评论界面分析响应体，找到请求评论信息的url
6.分析评论信息的url与特征信息的关联
7.伪造请求
'''

import json
import pandas as pd


def spiders(music_name: str, musician: str) -> None:
    path = 'comment_data'
    comment_list = []
    nick_list = []
    origin_url = "https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq" \
                 ".song&searchid=67497163474474686&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=" \
                 "10&w={}&g_tk_new_20200303=786184370&g_tk=786184370&loginUin=2240251279&hostUin=0&format=json&inCharset" \
                 "=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0".format(music_name)
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"
    }
    response = req.get(origin_url, headers=header)
    response.encoding = 'utf-8'
    data = json.loads(response.text)
    result = data.get('data').get('song').get('list')
    for i in result:
        if (i.get('singer')[0].get('name')).find(musician) != -1:
            temp = i.get('id')
            break
    for num in range(0, 20,1):
        url = "https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk_new_20200303=786184370&g_tk=786184370&loginUin" \
              "=2240251279&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0" \
              "&cid=205360772&reqtype=2&biztype=1&topid={}&cmd=8&needmusiccrit=0&pagenum={}&pagesize=25&lasthotcommentid" \
              "=&domain=qq.com&ct=24&cv=10101010".format(temp, num)
        response_ = req.get(url, headers=header)
        response.encoding = 'utf-8'
        comment_detail = json.loads(response_.text)
        for comment_ in comment_detail.get('comment').get('commentlist'):
            comment = comment_.get('rootcommentcontent')
            nick = comment_.get('nick')
            comment_list.append(comment)
            nick_list.append(nick)
    path = path + '/' + music_name + '.csv'
    dataframe = pd.DataFrame({'评论者': nick_list, '评论': comment_list})
    dataframe.to_csv(path, index=False, sep=',', encoding='utf_8_sig')


if __name__ == '__main__':
    music_name = "青花瓷".replace(" ", "")  # input("请输入歌名:")
    musician = "周杰伦"  # input("请输入歌手:")
    spiders(music_name, musician)
