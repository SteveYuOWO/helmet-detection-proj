import numpy as np
np.random.seed(1337)
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation, Convolution2D, MaxPooling2D, Flatten
from keras.optimizers import Adam

# download the mnist data
(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

# data pre-processing
X_train = X_train.reshape(-1, 1, 28, 28)
print(X_train.shape)
X_test = X_test.reshape(-1, 1, 28, 28)
print(X_test.shape)
Y_train = np_utils.to_categorical(Y_train, num_classes=10)
Y_test = np_utils.to_categorical(Y_test, num_classes=10)

# build CNN
model = Sequential()

# Conv layer 1 output shape (32, 28, 28)
model.add(Convolution2D(
    filters=32,
    kernel_size=(5, 5),
    # same 用0填充
    # valid 不填充
    padding='same',
    input_shape=(1, # channel
                 28, 28)  # height and width
))
model.add(Activation('relu'))

# Pooling layer 1 (max pooling) output shape (32, 14, 14)
model.add(MaxPooling2D(
    pool_size=(2, 2),
    # 步长
    strides=(2, 2),
    padding='same' # padding method
))

# Conv layer 2 output shape (64, 14, 14)
model.add(Convolution2D(filters=64, kernel_size=(5, 5), padding='same'))
model.add(Activation('relu'))

# Pooling layer 2 (max pooling) output shape (64, 7, 7)
model.add(MaxPooling2D(pool_size=(2, 2), padding='same'))

# Fully connected layer 1 input shape (64 * 7 * 7) = (3136)
# output shape (1024)
model.add(Flatten())
model.add(Dense(1024))
model.add(Activation('relu'))

# Fully connected layer 2 to shape (10) for 10 classes
model.add(Dense(10))
model.add(Activation('softmax'))

# Another way to define your optimiser
adam = Adam(lr=1e-4)

# add metrics to get more results you want to see
model.compile(optimizer=adam,
              loss='categorical_crossentropy',
              metrics=['accuracy'])

print('Training --------------------')
# Another way to train the model
model.fit(X_train, Y_train, nb_epoch=1, batch_size=32)
print('\nTesting --------------------')
loss, accuracy = model.evaluate(X_test, Y_test)

print('\ntest loss: ', loss)
print('\ntest accuracy: ', accuracy)

