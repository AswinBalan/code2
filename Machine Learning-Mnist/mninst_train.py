import tensorflow.keras as kr
import matplotlib.pyplot as pt
import tensorflow as tf

data = tf.keras.datasets.mnist

#download data
(x_t, y_t), (x_test,y_test) = data.load_data()

# print(x_t[0])

pt.imshow(x_t[0], cmap=pt.cm.binary)
pt.show()
print(y_t[0])
x_t = tf.keras.utils.normalize(x_t, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()


model.add(tf.keras.layers.Flatten())


model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_t,y_t,epochs=3)
loss, acc = model.evaluate(x_test,y_test)

print(loss, acc)
model.save('mnist_trained_model.model')

# pt.imshow(x_t[0], cmap=pt.cm.binary)
# pt.show()

