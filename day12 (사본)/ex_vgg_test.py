from keras.applications import vgg16
from keras.applications import vgg19
from keras.utils import load_img
from keras.utils import img_to_array
import matplotlib.pyplot as plt
import os

model = vgg16.VGG16()
# model2 = vgg19.VGG19()
print(model.summary())
# print(model2.summary())


def fn_predict_vgg(p_model, p_file):
    image = load_img(p_file, target_size=(224, 224))
    plt.imshow(image)
    plt.show()

    test_image = img_to_array(image).reshape((1, 224, 224, 3))
    test_image = vgg16.preprocess_input(test_image)

    yhat = p_model.predict(test_image)
    label = vgg16.decode_predictions(yhat)
    pred = label[0][0]
    print(pred[1], pred[2] * 100)


path = './imagenet/'
file_list = os.listdir(path)
for file in file_list:
    fn_predict_vgg(model, path + file)
