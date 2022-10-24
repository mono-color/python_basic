import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# IMDbs score
# r: 개별 영화 평점
# v: 개별 영화에 평점을 투표한 횟수
# m: 250위 안에 들어야 하는 최소 투표
# c: 전체 영화에 대한 평균 평점


def get_imdbs_score(p_x, p_m, p_c):
    p_v = p_x['cnt']
    p_r = p_x['avgScore']
    return (p_v / (p_v + p_m) * p_r) + (p_m / (p_m + p_v) + p_c)


df_ratings = pd.read_csv('../day20/data/ratings.csv')
df_movies = pd.read_csv('../day20/data/movies.csv')
# m 상위
df_mv = df_ratings[['movieId', 'rating']]
df_movies = pd.merge(df_movies, df_mv.groupby('movieId').mean(), right_on='movieId', left_index=True)
df_movies.rename(columns={'rating':'avgScore'}, inplace=True) # inplace true는 저장한다는 의미
print(df_movies.head())
df_movies = pd.merge(df_movies, df_mv.groupby('movieId').count(), right_on='movieId', left_index=True)
df_movies.rename(columns={'rating':'cnt'}, inplace=True)
print(df_movies.head())
# 평점 상위
m = df_movies['cnt'].quantile(0.9)
m_data = df_movies.copy().loc[df_movies['cnt'] >= m]
c = m_data['avgScore'].mean()
print('상위 10% 영화(투표기준)의 평균',m ,c)

m_data['score'] = m_data.apply(get_imdbs_score, args=(m, c), axis=1)
m_data['genres'] = m_data['genres'].apply(lambda x: x.replace('|', ' '))
m_data.reset_index(drop=True, inplace=True)
count_vector = CountVectorizer(ngram_range=(1,1))
genres_vector = count_vector.fit_transform(m_data['genres'])
print(genres_vector.toarray())
AA = genres_vector.toarray()
print(AA)
genres_sim = cosine_similarity(genres_vector, genres_vector).argsort()[:, ::-1]


def get_contentbase_movie(data, d_sim, title, top=20):
    target_movie_index = data[data['title'] == title].index.values
    sim_index = d_sim[target_movie_index, :top].reshape(-1)
    sim_index = sim_index[sim_index != target_movie_index]
    result = data.iloc[sim_index].sort_values('score', ascending=False)[:10]
    return result


while True:
    text = input('영화명:')
    result = get_contentbase_movie(m_data, genres_sim, text)
    for i, v in result.iterrows():
        print(result.loc[i]['title'], ":", result.loc[i]['genres'])

