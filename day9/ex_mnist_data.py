# pip install keras
# pip install tensorflow
# 만약에 CPU 만 사용한다면
# pip install tensorflow-cpu
# GPU 사용은 CUDA, cuDNN <-- 추가 설치해야함 .
import sys
from keras.datasets import mnist
from keras.utils import np_utils
(x_train, y_train), (x_test, y_test) = mnist.load_data()
import matplotlib.pyplot as plt
plt.imshow(x_train[1], cmap='Greys')
plt.show()
# 코드로 확인
for x in x_train[1]:
    for i in x:
        sys.stdout.write('%d\t' % i)
    sys.stdout.write('\n')
print('clss: %d' % y_train[1])