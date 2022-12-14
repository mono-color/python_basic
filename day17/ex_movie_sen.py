# DB에서 MV_REPLY 댓글과 MV_SCORE 7이상 긍정 1, 7 미만 부정0
#                댓글 null 제외
# DB에서 가져와서 X <-- 댓글
#               y <-- 0 or 1로 가져오시오


from konlpy.tag import Okt
from gensim.models import FastText, fasttext
import pandas as pd
from day5.mydb import Mydb
import numpy as np
from keras.preprocessing.text import Tokenizer
from keras_preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Flatten, Embedding, LSTM, Dropout

sql = """ 
 select CASE WHEN mv_score >=7 then 1
        when mv_score <7 then 0
        end as mv_score
        , trim(mv_reply) as mv_reply
from movie_reply
where mv_reply is not null"""

db = Mydb()
df = pd.read_sql(con=db.conn, sql=sql)
x_data = df['MV_REPLY'].values
y_data = df['MV_SCORE'].values
print(x_data)
print(y_data)
tokenizer = Tokenizer()
tokenizer.fit_on_texts(x_data)
VOCAB_SIZE = len(tokenizer.index_word) + 1
text_sequence = tokenizer.texts_to_sequences(x_data)
max_len = max(len(l) for l in text_sequence)
print(max_len)
pad_text = pad_sequences(text_sequence, maxlen=max_len, padding='post')
em_model = fasttext.FastText.load('../day16/fasttext_movie.model')


def get_vector(word, model):
    if word in model:
        return model[word]
    else:
        return None


wv = em_model.wv
embedding_matrix = np.zeros((VOCAB_SIZE, 200))
for word, i in tokenizer.word_index.items():
    temp = get_vector(word, wv.key_to_index)
    if temp is not None:
        embedding_matrix[i] = temp
print(embedding_matrix)
model = Sequential()
model.add(Embedding(VOCAB_SIZE, 200, input_length=max_len,
                    weights=[embedding_matrix], trainable=False))
model.add(Dropout(0.2))
model.add(LSTM(100, activation='tanh'))
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(pad_text, y_data, epochs=100)
print("\n acc : %.4f"%(model.evaluate(pad_text, y_data)[1]))


