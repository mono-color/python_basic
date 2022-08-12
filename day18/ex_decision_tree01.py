import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree
import matplotlib.pyplot as plt

# pip install graphviz
# 트리 시각화
# sudo apt-get install graphviz
iris = load_iris()
print(iris.feature_names)
print(iris.target_names)
print(iris.data[0])
print(iris.target[0])

test = [0, 50, 100]
train_data = np.delete(iris.data, test, axis=0)
train_y = np.delete(iris.target, test)

test_data = iris.data[test]
test_y = iris.target[test]

model = tree.DecisionTreeClassifier()
model.fit(train_data, train_y)

print('실제:', test_y)
print('예측:', model.predict(test_data))

data = iris.data[:, 0:2]
target = iris.target
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.plot(data[target == 0][:, 0], data[target == 0][:, 1], 'ro', label='setosa')
plt.plot(data[target == 1][:, 0], data[target == 1][:, 1], 'bo', label='versicolor')
plt.plot(data[target == 2][:, 0], data[target == 2][:, 1], 'yo', label='virginica')
plt.legend()
plt.show()

import graphviz
dot_data = tree.export_graphviz(model, out_file=None, feature_names=iris.feature_names
                                , class_names=iris.target_names
                                , filled=True, rounded=True, special_characters=True)
graph = graphviz.Source(dot_data)
graph.render('./iris', view=True)
print(graph)


