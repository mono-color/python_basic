from sklearn.preprocessing import LabelEncoder
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical

df = pd.read_csv('./iris.csv'
                 , names=['sepal_length', 'sepal_width'
                           , 'petal_length', 'petal_width', 'species'])
data = df.values
x = data[:, 0:4].astype(float)
y = data[:, 4]

encoder = LabelEncoder()
encoder.fit(y)
y = encoder.transform(y)
y_encoded = to_categorical(y)

model = Sequential()
model.add(Dense(64, input_dim=4, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(3, activation='softmax'))
model.compile(loss='categorical_crossentropy'
              , optimizer='adam'
              , metrics=['accuracy'])
model.fit(x, y_encoded, epochs=50)
print('\n acc: %.4f' % (model.evaluate(x, y_encoded)[1]))



