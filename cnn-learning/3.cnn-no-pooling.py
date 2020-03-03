from keras import models
from keras import layers
model_no_max_pool = models.Sequential()
model_no_max_pool.add(layers.Conv2D(32, (3,3), activation = "relu", input_shape= (28, 28, 1)))
model_no_max_pool.add(layers.Conv2D(64, (3,3), activation = "relu"))
model_no_max_pool.add(layers.Conv2D(64, (3,3), activation = "relu"))

model_no_max_pool.summary()
# 危害，计算量过大+因为不断训练扩张，导致局部性数据
