import numpy as np
import matplotlib.pyplot as plt

def h(x):
    return w0 + w1 * x

if __name__ == '__main__':
    # alpha学习率
    rate = 0.02

    # y = w0 * x + w1
    w0 = np.random.normal()
    w1 = np.random.normal()

    # 训练数据
    x_train = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
    y_train = np.array([1, 3, 4, 5, 6, 7, 8, 9, 10])

    err = 1
    # 计算误差函数
    while (err > 0.1):
        for (x, y) in zip(x_train, y_train):
            w0 -= (rate * (h(x) - y) * 1)
            w1 -= (rate * (h(x) - y) * x)

        # 代入找误差
        err = 0.0
        for (x, y) in zip(x_train, y_train):
            err += (y - h(x)) ** 2
        err /= float(x_train.size * 2)

    # 打印
    print("w0的值为%f" % w0)
    print("w1的值为%f" % w1)
    print("误差率的值为%f" % err)

    # 画图
    x = np.linspace(0, 10, 10)
    y = h(x)

    plt.figure()
    plt.plot(x_train, y_train, 'ro')
    plt.plot(x, y)
    plt.title("linear_regression")
    plt.xlabel('x')
    plt.ylabel('h(x)')
    plt.show()
