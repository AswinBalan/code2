import tensorflow.keras  as kr
import tensorflow as tf

import matplotlib.pyplot as pt

import numpy as np

import time

data = tf.keras.datasets.mnist
(x_t, y_t), (x_test,y_test) = data.load_data()
x_test = tf.keras.utils.normalize(x_test, axis=1)


test_model =  kr.models.load_model('mnist_trained_model.model')
predictions = test_model.predict(x_test)

print(len(x_test))
pt.imshow(x_test[100], cmap=pt.cm.binary)
pt.show()

time.sleep(5)

pt.close()
print(np.argmax(predictions[100]))
