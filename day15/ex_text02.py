import matplotlib.pyplot as plt
from konlpy.tag import Okt
from collections import Counter
import os
from wordcloud import WordCloud
# pip install palettable
from palettable.colorbrewer.qualitative import Dark2_8
import random
from PIL import Image
import numpy as np


def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
    return tuple(Dark2_8.colors[random.randint(0, 7)])


okt = Okt()
nouns = []
path = './newsData/4/'
for file in os.listdir(path):
    with open(path + file, 'r', encoding='utf-8') as f:
        text = f.read()
        nouns += okt.nouns(text)  # 명사만 추출
words = [n for n in nouns if len(n) > 1]
c = Counter(words)  # 단어들의빈도수 구함
icon = Image.open('./뉴스9.png')
mask = Image.new("RGB", icon.size, (255, 255, 255))
mask.paste(icon, icon)
mask = np.array(mask)
wc = WordCloud(font_path='BMHANNAPro.ttf', background_color='white'
               , width=400, height=400, scale=2.0, max_font_size=250, mask=mask)
gen = wc.generate_from_frequencies(c)
wc.recolor(color_func=color_func, random_state=3)
plt.figure('경제')
plt.imshow(gen)
wc.to_file('경제.png')
plt.show()
