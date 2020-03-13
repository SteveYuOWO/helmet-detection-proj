import numpy as np
import os
# macbook因为系统原因进行其设置
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
np.random.seed(1338)
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

'''create some data'''
# -1 到 1 之间取 200 个点
X = np.linspace(-1, 1, 200)
# x进行随机打乱
np.random.shuffle(X) # randomize the data
# np.random.normal(loc:均值, scale:标准差, size:大小)
Y = 0.5 * X + 2 + np.random.normal(0, 0.05, (200, ))

'''plot data'''
# plt.scatter 是绘制散点
plt.scatter(X, Y)
plt.show()

X_train, Y_train = X[:160], Y[:160]  # first 160 data
X_test, Y_test = X[160:], Y[160:]  # last 40 data

'''build a neural network from the 1st layer to the last layer'''
# 顺序建立的model
model = Sequential()
# layers属性是Dense, 输入1层，输出1层, 如果是多层，则不需要传递input参数
model.add(Dense(units=1, input_dim=1))

model.summary()

'''choose loss function and optimizing method'''
# 使用mse损失，gsd优化
model.compile(loss='mse', optimizer='sgd')

'''training'''
print("\ntraining --------")
for step in range(301):
    cost = model.train_on_batch(X_train, Y_train)
    if step % 100 == 0:
        print("train cost: ", cost)

'''test'''
print("\nTesting -------")
cost = model.evaluate(X_test, Y_test, batch_size=40)
print("test cost:", cost)
W, b = model.layers[0].get_weights()
print("Weights=", W, "\nbiases=", b)

# plotting the prediction
Y_pred = model.predict(X_test)
plt.scatter(X_test, Y_test)
plt.plot(X_test, Y_pred)
plt.show()