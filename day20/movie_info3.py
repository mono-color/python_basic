# -*- coding:utf-8 -*-
import re
from day5 import mydb
from bs4 import BeautifulSoup
import requests
import re


def fn_insert_reply():
    db = mydb.Mydb()
    movie_codes = []
    movie_data = []

    url = 'https://movie.naver.com/movie/bi/mi/basic.naver?code=210267'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    table = soup.select_one('.mv_info')
    title_tag = table.find('h3', class_='h_movie').select('a:first-child')[0]
    code = title_tag.get('href').split('=')[1]
    title = title_tag.text
    info_spec = table.select_one('.info_spec')
    genres_tags = info_spec.select_one('span').select('a')
    genres = ''
    for genre in genres_tags:
        if genre != genres_tags[-1]:
            genres += genre.text+', '
        else:
            genres += genre.text
    # print(code, title)
    actor = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(6)').text.replace('더보기', '')
    print(actor)
    director = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(4)').text
    print(director)
    if soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(8) > p > a'):
        grade = soup.select_one('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(8) > p > a')
        print(grade)
    spans = soup.select('#content > div.article > div.mv_info_area > div.mv_info > dl > dd:nth-child(2) > p > span')
    print(spans)
    time = spans[-2].text
    print(time)
    nation = spans[-3].select_one('a').text
    print(nation)

    movie_data.append([code, title, genres, actor, director, grade, time, nation])
    print(movie_data)


    # print(movie_data)
    # sql = """INSERT INTO movies (mv_code , mv_title , mv_genres , mv_actor , mv_director
    # , mv_grade , mv_time , mv_nation ) VALUES ( :v0 , :v1, :v2 , :v3 , :v4 , :v5 , :v6 , :v7 )"""
    # cnt = db.fn_insert_list(sql, movie_data)
    # print(cnt, '건 저장됨')


fn_insert_reply()
