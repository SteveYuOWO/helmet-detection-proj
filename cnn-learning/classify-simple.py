import numpy as np
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
np.random.seed(1337) # for reproducibility
from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop
import matplotlib.pyplot as plt

# download the mnist to the path '~/.keras/datasets/' if it is the first time to be called
# X shape ((60,000 28*28),  y shape (60,000, )
(X_train, Y_train),(X_test, Y_test) = mnist.load_data()

print("X_train shape (%d, %d, %d)" % X_train.shape)
print("Y_train shape (%d, )" % Y_train.shape)

# show images
plt.imshow(X_train[100])
print("The 100 label: %d" % Y_train[100])
plt.show()

# data pre-processing
X_train = X_train.reshape(X_train.shape[0], -1) / 255
X_test = X_test.reshape(X_test.shape[0], -1) / 255
Y_train = np_utils.to_categorical(Y_train, num_classes=10)
Y_test = np_utils.to_categorical(Y_test, num_classes=10)

# Another way to build your neural net
model = Sequential([
    Dense(units = 32, input_dim = 784),
    Activation('relu'),
    Dense(units = 10),
    Activation('softmax')
])

# Another way to define tour optimizer
rmsprop = RMSprop(learning_rate = 0.001, rho = 0.9, epsilon = 1e-8, decay = 0.0)

# We add metrics to get more results tou want to see
model.compile(
    optimizer = rmsprop,
    loss = 'categorical_crossentropy',
    metrics = ['accuracy'],
)

print("Training ----------")

# Another way to train the model
model.fit(X_train, Y_train, nb_epoch = 2, batch_size = 32)

print("\nTesting ----------")
# Another way to train the model
loss, accuracy = model.evaluate(X_test, Y_test)


print("test loss:", loss)
print("test accuracy:", accuracy)


