# -*- coding:utf-8 -*-
import re

from bs4 import BeautifulSoup
import requests


def fn_write_txt(text):
    f = open('movie_info.txt', 'a')
    f.write(text)
    f.writelines('\n')
    f.close()


for i in range(10):
    url = 'https://movie.naver.com/movie/point/af/list.naver?&page=1'#+str(i)
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'html.parser')
    # 구조화되게 출력
    # print(soup.prettify())
    table = soup.select_one('.list_netizen')
    trs = table.find_all('tr')
    for tr in trs:
        a = tr.select_one('.title a')
        if a:
            title = a.text
            url = a.get('href')
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

            info = "제목:{0} 평점:{1} 영화평가:{2} 평가자ID:{3} 상세정보:{4} 날짜:{5}".format(title, score, reply, user, url, day)
            print(info)
            # fn_write_txt(info)
