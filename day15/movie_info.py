# -*- coding:utf-8 -*-
import re
from day5 import mydb
from bs4 import BeautifulSoup
import requests


def fn_insert_reply():
    for i in range(1000):
        url = 'https://movie.naver.com/movie/point/af/list.naver?&page={0}'.format(str(i))
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        db = mydb.Mydb()
        table = soup.select_one('.list_netizen')
        trs = table.find_all('tr')
        movie_data = []
        for tr in trs:
            a = tr.select_one('.title a')
            if a:
                title = a.text
                url = a.get('href')
                code = url.split('&')[1]
                em = tr.select_one('.list_netizen_score em')
                score = em.text

                td = tr.select_one('.title')
                text_tag = str(td).split('<br/>')
                if len(text_tag) > 1:
                    msg = text_tag[1].split('\n')
                    reply = msg[0].strip()
                else:
                    pass
                user = tr.select_one('.author').text
                td2 = tr.select_one('.num:last-child')
                text_tag2 = str(td2).split('<br/>')
                if len(text_tag2) > 1:
                    date = text_tag2[1].split('<')
                    if len(date) > 1:
                        day = re.sub(r'[^0-9.]', '', date[0])
                movie_data.append([title, code, score, reply, day])
        print(movie_data)
        sql = """INSERT INTO movie_reply (num, title, mv_code, mv_score, mv_reply
                , mv_date) VALUES (movie_rep_seq.nextval, :1, :2, :3, :4, :5)"""
        cnt = db.fn_insert_list(sql, movie_data)
        print(cnt, '건 저장됨')


fn_insert_reply()
