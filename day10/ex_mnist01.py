import os.path
import sys
from keras.datasets import mnist
from keras.models.cloning import Sequential
from keras.utils import np_utils
import matplotlib.pyplot as plt
import tensorflow as tf
from keras.layers import Dense

# seed 값 설정(똑같은 랜덤 값 나오도록)
tf.random.set_seed(0)
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# plt.imshow(x_train[1], cmap='Greys')

x_train = x_train.reshape(x_train.shape[0], 784).astype('float32') / 255
x_test = x_test.reshape(x_test.shape[0], 784).astype('float32') / 255
# 정답 숫자를 labeling
y_train = np_utils.to_categorical(y_train)
y_test = np_utils.to_categorical(y_test)
model = Sequential()
model.add(Dense(512, input_dim=784, activation='relu'))
model.add(Dense(10, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics='accuracy')
model.summary()
# model.fit(x_train, y_train, epochs=30, batch_size=200)
# model.save('first_model.model')
# 모델 저장
MODEL_DIR = './model/'
if not os.path.exists(MODEL_DIR):
    os.mkdir(MODEL_DIR)
modelpath = './model/{epoch:02d}-{val_loss:.4f}.hdf5'
from keras.callbacks import ModelCheckpoint, EarlyStopping

checkpoint = ModelCheckpoint(filepath=modelpath, monitor='val_loss'
                             , verbose=1, save_best_only=True)
# 10회 이상 동일하면 멈춤
early_stop = EarlyStopping(monitor='val_loss', patience=10)
history = model.fit(x_train, y_train, epochs=30
                    , batch_size=200
                    , validation_data=(x_test, y_test)
                    , callbacks=[early_stop, checkpoint])
# 테스트 정확도 출력
print('\n test acc: %.4f' % model.evaluate(x_test, y_test)[1])
# 테스트 셋 오차
y_test_loss = history.history['val_loss']
# 학습 데이터 오차
y_loss = history.history['loss']
# 그래프로 표현
import numpy as np

xlen = np.arange(len(y_loss))
plt.plot(xlen, y_test_loss, marker='.', c='red', label=1000)
plt.plot(xlen, y_loss, marker='.', c='blue', label=1000)
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()
