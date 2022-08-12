# pip install tensorflowjs
import tensorflowjs as tfjs
from keras.models import load_model
model = load_model('../day13/model/vgg16_dental.h5')
tfjs.conve