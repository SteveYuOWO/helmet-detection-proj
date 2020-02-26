# CNN learning

### ❤️Introduction

项目课题基于CNN介绍

### 🧡What Keras?

**Keras**是一个用Python编写的开源神经网络库。设计用于实现深度神经网络的快速实验，它的重点是用户友好，模块化和可扩展。它是ONEIROS（开放式神经电子智能机器人操作系统）项目研究工作的一部分，其主要作者和维护者是Google的FrançoisChollet工程师。Chollet还是XCeption深度神经网络模型的作者。

下面的案例我们会了解Keras在神经网络编程的方便性

### 🧡What CNN?

神经网络由一连串的神经层组成，每一层存在很多神经元。

每一个神经网络都有输入和输出值。

🤠举例：Linear Regression

⚙️这个文件我进行了详细的标注。[keras_test/regression.py](regression.py) 

🤠举例：Image Classification

图片识别的过程中，不是色彩缤纷的图案，而是一堆堆的数字。当神经网络需要处理信息的时候，即是发挥优势的时候。

✅卷积不再对每个像素进行处理，而是对每一小块区域进行处理。✅这样增强了图片信息的连续性，使得神经网络能看到图形，而非一个点。✅具体来说，卷积神经网络有一个批量过滤器。

⚙️自带的mnist训练图片识别。[keras_test/classify-simple](classify-simple.py) 

### 💛What IC & OD?

✅Image Classification: 图像识别，对单图进行识别。比如：识别图片猫、识别图片小狗

✅Object Detection: 物体检测，对图片中物体进行检测。比如：识别图片中的食物、衣物。

实际上。我们想对安全帽进行的是Object Detection的工作

### 💚How CNN?

自然，我们知道了现代化的框架，例如Keras可以让深度学习变简单。但是，我们依然需要了解深度学习流程。

![](https://img2018.cnblogs.com/blog/1449595/202002/1449595-20200227024749399-985580982.png)

这张图很好描述了流程。

 **✅数据输入层/Input layer**

我们左边的图片输入是Input layer处理图片的输入。

这边，我们要处理的是图片的去均值、归一化、去相关、白化操作

- 🤠去均值：把输入数据各个维度都中心化为0，如下图所示，其目的就是把样本的中心拉回到坐标系原点上。
- 🤠归一化：幅度归一化到同样的范围，如下所示，即减少各维度数据取值范围的差异而带来的干扰，比如，我们有两个维度的特征A和B，A范围是0到10，而B范围是0到10000，如果直接使用这两个特征是有问题的，好的做法就是归一化，即A和B的数据都变为0到1的范围。
- 🤠PCA/白化：用PCA降维；白化是对数据各个特征轴上的幅度归一化

![](https://img2018.cnblogs.com/blog/1449595/202002/1449595-20200227025436057-730971864.png)

<p align="center">zoo-centered normalized data</p>

![](https://img2018.cnblogs.com/blog/1449595/202002/1449595-20200227050443095-753146459.png)

<p align="center">decorrelated whitened data</p>

 **✅卷积计算层/CONV layer**

这一层就是卷积神经网络最重要的一个层次，也是“卷积神经网络”的名字来源。
在这个卷积层，有两个关键操作：

- 局部关联。每个神经元看做一个滤波器(filter)
- 窗口(receptive field)滑动， filter对局部数据计算

![](https://img2018.cnblogs.com/blog/1449595/202002/1449595-20200227025617295-1875760932.png)

**✅ 激励层/Activation layer**

把卷积层输出结果做非线性映射。

CNN采用的激励函数一般为ReLU(The Rectified Linear Unit/修正线性单元)，它的特点是收敛快，求梯度简单，但较脆弱，图像如下。

![](https://img2018.cnblogs.com/blog/1449595/202002/1449595-20200227025928589-443439138.png)

激励层的实践经验：

- ①不要用sigmoid！不要用sigmoid！不要用sigmoid！
- ② 首先试RELU，因为快，但要小心点
- ③ 如果2失效，请用Leaky ReLU或者Maxout
- ④ 某些情况下tanh倒是有不错的结果，但是很少

**✅ 池化层/Pooling layer**

池化层夹在连续的卷积层中间， 用于压缩数据和参数的量，减小过拟合。
简而言之，如果输入是图像的话，那么池化层的最主要作用就是压缩图像。

![](https://img2018.cnblogs.com/blog/1449595/202002/1449595-20200227030055296-1820233911.png)

池化层用的方法有Max pooling 和 average pooling，而实际用的较多的是Max pooling。

这里就说一下Max pooling，其实思想非常简单。

![](https://img2018.cnblogs.com/blog/1449595/202002/1449595-20200227030122648-536118045.png)

对于每个2\*2的窗口选出最大的数作为输出矩阵的相应元素的值，比如输入矩阵第一个2\*2窗口中最大的数是6，那么输出矩阵的第一个元素就是6，如此类推。

**✅ 全连接层/Full Connection**

两层之间所有神经元都有权重连接，通常全连接层在卷积神经网络尾部。也就是跟传统的神经网络神经元的连接方式是一样的

![](https://img2018.cnblogs.com/blog/1449595/202002/1449595-20200227030248875-1746334058.png)

**一般流程:**

```
1. INPUT
2. [[CONV -> RELU]*N -> POOL?]*M
3. [FC -> RELU]*K
4. FC
```

### 💙Object Detection Technology

Object Detection 技术的演进：

```
RCNN -> SppNET -> Fast-RCNN ->Faster-RCNN
```

这段不过多介绍，Object Detection 原理基于 Image Classification，简单说，我们可以枚举所有可能的Object进行Image Classification，科学家发明好多选定候选框的方法，比如EdgeBoxes和Selective Search。

以下是各种选定候选框的方法的性能对比。

![](https://img2018.cnblogs.com/blog/1449595/202002/1449595-20200227031353286-708646793.png)

目前Faster-RCNN能够达到视频流处理的效果

### ❤️参考文献

- [莫烦Python blog](https://morvanzhou.github.io/)

- [冠军的试炼: 卷积神经网络CNN总结](https://www.cnblogs.com/skyfsm/p/6790245.html)
- [Keras Documention](https://keras.io/)
- [基于深度学习的目标检测技术演进](https://www.cnblogs.com/skyfsm/p/6806246.html)

