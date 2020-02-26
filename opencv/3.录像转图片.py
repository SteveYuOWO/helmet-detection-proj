# -*- coding:utf-8 -*-
# 录像转换为图片
from time import gmtime, strftime
import cv2
videoFile = '/Users/steveyu/Documents/build-blog.m4v'
cap = cv2.VideoCapture(videoFile)
cap.set(3,640)
cap.set(4,480)


while(True):
    ret, frame = cap.read()
    img = frame
    cv2.imshow('my', img)
    f = strftime("%Y%m%d%H%M%S.jpg", gmtime())
    cv2.imwrite('output/'+ f, img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if img.size == 0:
        break
    cap.release
    cv2.destroyAllWindows()