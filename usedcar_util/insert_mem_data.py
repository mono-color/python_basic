from day5 import mydb
import random

db = mydb.Mydb()
sql = """INSERT INTO members (mem_name, mem_id, mem_pass, mem_age, mem_sex
        , mem_job, mem_hobby, mem_phone, mem_mail) VALUES (
        :v0, 'a'||LPAD(id_seq.nextval,3,0), 1234, :v1, :v2, :v3, :v4, '010-1234-5678', null)"""

for i in range(100):
    women = ['김이나', '이민아', '박설리', '송나겸', '김태리', '홍수아', '오지혜', '최윤정', '나희경', '김주희']
    men = ['한예성', '황의창', '김달현', '염현섭', '임요한', '유호동', '최강인', '홍익현', '나그네', '방구남']
    hobby = ['캠핑', '영화', '등산', '수영', '여행', '게임', '캠핑', '캠핑', '독서', '게임']
    job_w = ['주부', '개발자', '영업', '연구원', '공무원', '배우', '회사원', '자영업', '회사원', '주부']
    job_m = ['자영업', '개발자', '영업', '연구원', '공무원', '배우', '회사원', '기사', '회사원', '회사원']
    age = str(random.randint(20, 60))

    ran_w = random.randint(0, 9)
    ran_m = random.randint(0, 9)
    ran_h = random.randint(0, 9)
    ran_j = random.randint(0, 9)
    people_w = [
        women[ran_w], age, '여', job_w[ran_j], hobby[ran_h]
    ]
    people_m = [
        men[ran_m], age, '남', job_m[ran_j], hobby[ran_h]
    ]
    # print(people)
    # db.fn_insert(sql, people_w)
    db.fn_insert(sql, people_m)
    print('삽입 완료')
