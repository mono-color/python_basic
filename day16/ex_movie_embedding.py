from konlpy.tag import Okt
from gensim.models import word2vec
import pandas as pd
from wordcloud import WordCloud
from day5 import mydb

db = mydb.Mydb()
okt = Okt()
sql = """ 
        SELECT title|| ' 영화는 ' || trim(mv_reply) as mv_reply
            from movie_reply
            where mv_reply is not null
"""

df = pd.read_sql(sql, con=db.conn)
result = []
for i, v in df.iterrows():
    text = okt.pos(v['MV_REPLY'], norm=True, stem=True)  # pos: 각 단어에 접근해서 형태소 분석하는 것(parsing)
    re = []
    for word in text:
        if not word[1] in ["Josa", "Modifier", "Punctuation", "Emoi"]:
            re.append(word[0])
        rl = (" ".join(re)).strip()
        result.append(rl)
print(result)
nlp_data = "movie.nlp"
with open(nlp_data, 'w', encoding='utf-8') as f:
    f.write('\n'.join(result))
wData = word2vec.LineSentence(nlp_data)
model = word2vec.Word2Vec(wData, sg=1, vector_size=200, window=3, min_count=3, workers=4)
model.save('movie.model')
