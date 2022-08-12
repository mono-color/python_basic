import matplotlib.pyplot as plt
from konlpy.tag import Okt
from wordcloud import WordCloud
from day5 import mydb
import pandas as pd
from collections import Counter

okt = Okt()
nouns = []
db = mydb.Mydb()
sql = """ 
        SELECT trim(mv_reply) as mv_reply
            from movie_reply
            where title like '%'||:nm||'%'
            and mv_reply is not null
"""

while True:
    nm = input('영화 제목을 입력하세요(종료q):')
    if 'q' == nm:
        break
    else:
        df = pd.read_sql(sql, con=db.conn, params={"nm": nm})
        print(df.head())
        for i, v in df.iterrows():
            nouns += okt.nouns(v['MV_REPLY'])  # 명사만 추출
        words = [n for n in nouns if len(n) > 1]
        c = Counter(words)
        wc = WordCloud(font_path='./BMHANNAPro.ttf', width=400, height=400, scale=2.0, max_font_size=250)
        gen = wc.generate_from_frequencies(c)
        plt.figure('영화명')
        plt.imshow(gen)
        wc.to_file('영화명.png')
        plt.show()

