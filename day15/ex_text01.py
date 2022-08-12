# pip install wordcloud
# pip install konlpy
# pip install gensim
import matplotlib.pyplot as plt
from konlpy.tag import Okt
from collections import Counter
import os
from wordcloud import WordCloud
# 한국어 parser

okt = Okt()
nouns = []
path = './newsData/1/'
for file in os.listdir(path):
    with open(path + file, 'r', encoding='utf-8') as f:
        text = f.read()
        nouns += okt.nouns(text)  # 명사만 추출
words = [n for n in nouns if len(n) > 1]
c = Counter(words)  # 단어들의빈도수 구함
print(c)
wc = WordCloud(font_path='./BMHANNAPro.ttf', width=400, height=400, scale=2.0, max_font_size=250)
gen = wc.generate_from_frequencies(c)
plt.figure('경제')
plt.imshow(gen)
wc.to_file('경제.png')
plt.show()
