import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv('./Mall_Customers.csv')
df['Gender'] = df['Gender'].map({'Female': 1, 'Male': 0})
data = df[['Gender', 'Age', 'Annual Income', 'Spending Score']]

print(df.columns)
print('=====')
print(df.info())
print('=====')
print(df.describe())

num_cluster = list(range(1, 11))
inertias = []
# inertia_ <-- 는 군집의 중심 centroid 와 각 사이의 거리를 나타냄
# inertia_가 낮은 그룹을 좋은 그룹이라 할 수 있음 이러한 그룹을 적게 만들수록 좋은 군집화 모델
for i in num_cluster:
    model = KMeans(n_clusters=i)
    model.fit(data)
    inertias.append(model.inertia_)
plt.plot(num_cluster, inertias, '-o')
plt.xlabel('number of cluster (k)')
plt.ylabel('inertia')
plt.show()
