#! /usr/bin/env python3
from os import path
from wordcloud import WordCloud
import tkinter as TK
d =  path.dirname(__file__)

text =  open(path.join(d,'word.txt')).read()

wordcloud = WordCloud().generate(text)


import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

wordcloud = WordCloud(max_font_size=30).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show() 


