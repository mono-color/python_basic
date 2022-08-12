import pandas as pd
from sklearn import tree
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('./playing golf.csv')
print(df.columns)
train_x = df[['outlook', 'temperature', 'humidity', 'windy']]
train_y = df['play']

# labeling
enc_class = {}


def encoding_label(x):
    labeler = LabelEncoder()
    labeler.fit(x)
    label = labeler.transform(x)
    enc_class[x.name] = labeler.classes_
    return label


train_x = train_x[train_x.columns].apply(encoding_label)
print(train_x)

model = tree.DecisionTreeClassifier()
model.fit(train_x, train_y)

import graphviz

dot_data = tree.export_graphviz(model, out_file=None
                                , feature_names=train_x.columns.values.tolist()
                                , class_names=train_y.drop_duplicates().values.tolist()
                                , filled=True, rounded=True, special_characters=True)
graph = graphviz.Source(dot_data)
graph.render('./golf', view=True)
print(graph)
print(enc_class)
test = pd.DataFrame({"outlook": 1, "temperature": 1, "humidity": 0, "windy": 0}, index=[0])
print("테스트:", model.predict(test))
print("테스트:", model.predict_proba(test))
