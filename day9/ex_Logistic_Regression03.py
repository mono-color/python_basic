# 피마 인디언 데이터 (당뇨병 예측)
#
# 임신횟수, 포도당 수치, 혈압, 피부두께, 인슐린, BMI, 당뇨병가족력, 나이
# 당뇨병 여부 (0:아님, 1:당뇨) <-- 종속 변수 이항분류
import pandas as pd
df = pd.read_csv('../day8/datasets/pima-indians-diabetes.csv')
print(df.info())

x = df.iloc[:, 0:8]
de = x.describe()
print(de)
y = df.iloc[:, 8]
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2)
model = LogisticRegression(max_iter=50000)
train_x = scaler.fit_transform(train_x)
test_x = scaler.fit_transform(test_x)
model.fit(train_x, train_y)
print(model.coef_)
print(model.intercept_)
print(model.score(train_x, train_y))
print(model.score(test_x, test_y))
