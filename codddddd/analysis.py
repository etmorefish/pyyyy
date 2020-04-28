import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from snownlp import SnowNLP
from wordcloud import WordCloud
plt.style.use('ggplot')
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

music_name = "青花瓷"
path = 'comment_data/{}.csv'.format(music_name)
csv_data = pd.read_csv(path)
comment = list(dict(csv_data).get("评论"))
l = []
labels_positive = []
labels_negative = []
key = []
for i in comment:
    rate = SnowNLP(i)  # 获得评论情感表示值[0,1]越大越正向
    temp = rate.sentiments
    key_ = []
    for k in rate.keywords():
        if '[' not in k:
            key_.append(k)

    key.append(','.join(key_))
    l.append(temp)
    if temp >= 0.5:
        labels_positive.append(1)
    else:
        labels_negative.append(1)

array = np.asarray(l, dtype='float64')

labels_negative_array = np.asarray(labels_positive, dtype='int32')
labels_positive_array = np.asarray(labels_negative, dtype='int32')

negative_sum = labels_negative_array.sum()  # 正向评论标签
positive_sum = labels_positive_array.sum()  # 负向评论标签

plt.hist(l, bins=np.arange(0, 1.01, 0.01), label='分部图', color='#1890FF')
plt.xlabel("semiscore")
plt.ylabel("number")
plt.title("正负向评论分布图")
plt.show()

plt.bar([1, -1], [negative_sum, positive_sum], tick_label=[1, -1], color='#2FC25B')
plt.xlabel("semislabel")
plt.ylabel("number")
plt.title("正负向评论对比图")
plt.show()

# 生成词云图
wordcloud = WordCloud(font_path="../simhei.ttf",
                      background_color="black", width=600,
                      height=300, max_words=50).generate(''.join(key))

image = wordcloud.to_image()
image.show()
