# CNN

##### 参考：https://www.bilibili.com/video/av16175135?from=search&seid=14672179579223724752

### Step1.Convolution

The image do the same process for every filter. Then we will get The Feature Map.

The value of Filter is called weight.

### 卷积作用：取的是局部特征

### 一般卷积需要进行一步relu，relu的函数 y=max(0, y)，为了去掉非0值

### 理由：非0的铁定不是特征

![](https://img2020.cnblogs.com/blog/1449595/202003/1449595-20200312174957006-1592385752.png)



![](https://img2020.cnblogs.com/blog/1449595/202003/1449595-20200312175103999-1762221347.png)



### Step2.MaxPooling

### 最大池化的作用：使得特征更明显

科学家研究发现：经过Convolution卷积，会丢失一些信息，之后，我们使用MaxPooling对信息进行增强

##### 理由：在色域中，最大色值往往与人眼睛看的一样，比如：你看一个叶子是绿色的，那么这个G值会最大。我们仅需要保存这9个值中的G值即可，忽略其他小的

![](https://img2020.cnblogs.com/blog/1449595/202003/1449595-20200312175523322-78457023.png)

![](https://img2020.cnblogs.com/blog/1449595/202003/1449595-20200312175606907-283150552.png)

![](https://img2020.cnblogs.com/blog/1449595/202003/1449595-20200312180108021-1531064547.png)



### CNN in Keras

```python
// (25, 3, 3) 25个filter，3 * 3的matrix
// (1, 28, 28) 1代表黑白的， 3为r, g, b pixel
model2.add(Convolution2D(25, 3, 3), input_shape(1, 28, 28))
// 得到了25 * 26 * 26
model2.add(MaxPooling2D((2, 2)))
// 得到了25 * 13 * 13
model2.add(Convolution2D(50, 3, 3), input_shape(1, 28, 28))
// 得到了25 * 11 * 11
model2.add(MaxPooling2D((2,2)))
model2.add(Dense(output_dim=100))
model2.add(Activation('relu'))
model2.add(Dense(output_dim=10))
model2.add(Activation('softmax'))
```

![](https://img2020.cnblogs.com/blog/1449595/202003/1449595-20200312185006484-691614060.png)



### 以上重复N次

### Fully conneted layer

**Vote depends on how strongly a value predicts X or O**

### 这步理解比较难，主要是把部分特征进行拼合，我们进行

![](https://img2020.cnblogs.com/blog/1449595/202003/1449595-20200313140101572-1154364455.png)































