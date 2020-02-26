import cv2 as cv
import numpy as np


def get_image_info(image):
    print(type(image))
    # 宽 高 通道数量
    print(image.shape)
    # 大小（shape三元祖的乘积）
    print(image.size)
    # data type
    print(image.dtype)
    # np数组
    print(np.array(image))


if __name__ == '__main__':
    src = cv.imread("timg.jpeg")
    # cv.namedWindow("input image", cv.WINDOW_AUTOSIZE)
    cv.imshow("image", src)
    get_image_info(src)
    # 无限显示，不限定时间
    cv.waitKey(0)
    cv.destroyAllWindows()
    # 转为灰度图像
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    # 写出图片
    cv.imwrite("../img/result2.png", gray)
    print("hi, python")
