import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv('./Mall_Customers.csv')
data = df.iloc[:, [3, 4]].values
# df['Gender'] = df['Gender'].map({'Female': 1, 'Male': 0})
# data = df[['Gender', 'Age', 'Annual Income', 'Spending Score']]

model = KMeans(n_clusters=5, init='k-means++', max_iter=300, n_init=5, random_state=8)
pred = model.fit_predict(data)

plt.scatter(data[pred == 0, 0], data[pred == 0, 1], s=100, c='pink', label='miser')
plt.scatter(data[pred == 1, 0], data[pred == 1, 1], s=100, c='yellow', label='general')
plt.scatter(data[pred == 2, 0], data[pred == 2, 1], s=100, c='cyan', label='target')
plt.scatter(data[pred == 3, 0], data[pred == 3, 1], s=100, c='magenta', label='spendthrift')
plt.scatter(data[pred == 4, 0], data[pred == 4, 1], s=100, c='orange', label='careful')
plt.scatter(model.cluster_centers_[:, 0], model.cluster_centers_[:, 1], s=50, c='blue', label='ce??')
plt.style.use('fivethirtyeight')
plt.title('k means cluster', fontsize=20)
plt.xlabel('annual income')
plt.ylabel('spending score')
plt.legend()
plt.grid()
plt.show()
