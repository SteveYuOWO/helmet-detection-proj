from keras.datasets import mnist
from keras import models
from keras import layers
from keras.utils import to_categorical


'''prepare data'''
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
# 归一化
train_images = train_images.reshape(60000, 28 * 28)
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape(test_images.shape[0], -1)
'''prepare label'''
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

'''build layer and model'''
network = models.Sequential()

# relu, softmax
# relu 函数的作用就是增加了神经网络各层之间的非线性关系 激活
# 512 是输出的维度
network.add(layers.Dense(512, activation='relu', input_shape=(28 * 28,)))
# softmax 在二分类问题中引入概率
network.add(layers.Dense(10, activation='softmax'))

'''set loss optimizer metrics'''
# loss: 保证在训练数据上性能的前进
# optimizer: 基于训练数据和损失更新网络机制
# metric: 训练中的指标, 本案例描述正确的比率
network.compile(optimizer = 'rmsprop', loss = 'categorical_crossentropy', metrics = ['accuracy'])

### optimizer函数有
# sgd 随机梯度下降
# momentum 移动指数加权平均(平滑处理的，让梯度的摆动幅度变得更小）
# RMSProp 微分平方加权平均数
# adam momentum+rmsprop 需要初始化梯度的累积量和平方累积量

# 开始拟合
# 单次训练迭代5次
# 批量128处理
network.fit(train_images, train_labels, epochs = 5, batch_size = 128)
# loss 损失, acc 成功率
test_loss, test_acc = network.evaluate(test_images, test_labels)
print('loss: %.2f' % test_loss)
print('acc: %.2f' % test_acc)


