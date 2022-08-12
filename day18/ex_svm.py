import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix

iris = datasets.load_iris()
x = iris.data
y = iris.target
class_name = iris. target_names
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0, test_size=0.2)
model = svm.SVC(kernel='linear', C=0.01).fit(x_train, y_train)

np.set_printoptions(precision=2)
title_option = [('confusion matrix, without normalization', None)
                , ('normalized confusion matrix', 'true')]
for title, normalize in title_option:
    disp = plot_confusion_matrix(model, x_test, y_test
                                 , display_labels=class_name
                                 , cmap=plt.cm.Blues
                                 , normalize=normalize)
    disp.ax_.set_title(title)
    print(title)
    print(disp.confusion_matrix)
plt.show()
