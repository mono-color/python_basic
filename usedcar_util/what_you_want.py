from day5 import mydb
import pandas as pd

# db = mydb.Mydb()
# sql = """SELECT buyer_age, buyer_sex, buyer_job, buyer_hobby FROM sell_history"""
# mem_info = db.get_select(sql)
# print(mem_info)

from keras.utils import to_categorical

df = pd.read_csv('sell_history.csv')

df['BUYER_SEX'] = df['BUYER_SEX'].map({'남': 1, '여': 0})
df['BUYER_JOB'] = df['BUYER_JOB'].map(
    {'주부': 0, '기사': 1, '개발자': 2, '영업': 3, '연구원': 4, '공무원': 5, '배우': 6, '회사원': 7, '자영업': 8})
df['BUYER_HOBBY'] = df['BUYER_HOBBY'].map({'캠핑': 0, '영화': 1, '등산': 2, '수영': 3, '여행': 4, '게임': 5, '독서': 6})
gender = to_categorical(df['BUYER_SEX'].tolist(), len(df['BUYER_SEX'].drop_duplicates()))
job = to_categorical(df['BUYER_JOB'].tolist(), len(df['BUYER_JOB'].drop_duplicates()))
hobby = to_categorical(df['BUYER_HOBBY'].tolist(), len(df['BUYER_HOBBY'].drop_duplicates()))
gender_names = ["gen1", "gen2"]
job_names = ["job1", "job2", "job3", "job4", "job5", "job6", "job7", "job8", "job9"]
hobby_names = ["hobby1", "hobby2", "hobby3", "hobby4", "hobby5", "hobby6", "hobby7"]

data_gen = pd.DataFrame(gender, columns=gender_names)
data_job = pd.DataFrame(job, columns=job_names)
data_hobby = pd.DataFrame(hobby, columns=hobby_names)
data_df = pd.concat([data_gen, data_job, data_hobby], axis=1)

from sklearn.metrics.pairwise import cosine_similarity

user_base_metric = cosine_similarity(data_df)

while True:
    id = input('user id:')
    id = df[df['BUYER_ID'] == id].index.values[0]
    user_base_metric_df = pd.DataFrame(data=user_base_metric, index=df.index
                                       , columns=df.index)

    sim_user = user_base_metric_df[id].sort_values(ascending=False)[:5]
    id_list = sim_user.index.tolist()[1:]
    print('내가 관심있는차 브랜드:', df.loc[id]['CAR_BRAND'], '/이름:', df.loc[id]['CAR_NAME'], '/크기:', df.loc[id]['CAR_SIZE'])
    sim = df.loc[id_list]
    print(sim)
