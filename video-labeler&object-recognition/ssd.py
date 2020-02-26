# # -*-coding: utf-8-*-
# from keras.preprocessing import image
# from keras.applications.imagenet_utils
# import preprocess_input from scipy.misc
# import imread
# import numpy as np
# from ssd import SSD300
# from ssd_utils import BBoxUtility
# import matplotlib.pyplot as plt
# import cv2
# from os import listdir
#  voc_classes = ['Aeroplane', 'Bicycle', 'Bird', 'Boat', 'Bottle',
#  'Bus', 'Car', 'Cat', 'Chair', 'Cow', 'Diningtable',
#  'Dog', 'Horse','Motorbike', 'Person', 'Pottedplant',
#  'Sheep', 'Sofa', 'Train', 'Tvmonitor']
# NUM_CLASSES = len(voc_classes) + 1
# input_shape=(300, 300, 3)
# model = SSD300(input_shape, num_classes=NUM_CLASSES) model.load_weights('weights_SSD300.hdf5', by_name=True)
# bbox_util = BBoxUtility(NUM_CLASSES)
#  def ssd(img_path):
# global oPath
# inputs = []
# images = []
# #img_path = 'test02.jpg'
# img0 = cv2.imread(img_path)
# img = image.load_img(img_path, target_size=(300, 300))
# img = image.img_to_array(img)
#  images.append(imread(img_path))
# inputs.append(img.copy())
# inputs = preprocess_input(np.array(inputs))
# preds = model.predict(inputs, batch_size=1, verbose=1)
# results = bbox_util.detection_out(preds)
# #print results
# # Parse the outputs.
# for i, img in enumerate(images):
# det_label = results[i][:, 0]
# det_conf = results[i][:, 1]
# det_xmin = results[i][:, 2]
# det_ymin = results[i][:, 3]
# det_xmax = results[i][:, 4]
# det_ymax = results[i][:, 5]
# #print i,det_label,det_conf
# # Get detections with confidence higher than 0.6.
# top_indices = [i for i, conf in enumerate(det_conf) if conf >= 0.5]
# top_conf = det_conf[top_indices]
# top_label_indices = det_label[top_indices].tolist()
# top_xmin = det_xmin[top_indices]
# top_ymin = det_ymin[top_indices]
# top_xmax = det_xmax[top_indices]
# top_ymax = det_ymax[top_indices]
#  #colors = plt.cm.hsv(np.linspace(0, 1, 21)).tolist()
# #plt.imshow(img / 255.)
# #currentAxis = plt.gca()
# #print top_label_indices
# #print top_conf
# #print top_conf.shape[0]
# for i0 in range(top_conf.shape[0]):
# xmin = int(round(top_xmin[i0] * img.shape[1]))
#
# ymin = int(round(top_ymin[i0] * img.shape[0]))
# xmax = int(round(top_xmax[i0] * img.shape[1]))
# ymax = int(round(top_ymax[i0] * img.shape[0]))
#
# score = top_conf[i0]
#  label = int(top_label_indices[i0])
# label_name = voc_classes[label - 1]
# #display_txt = '{:0.2f}, {}'.format(score, label_name)
# #coords = (xmin, ymin), xmax-xmin+1, ymax-ymin+1
# #color = colors[label]
# #currentAxis.add_patch(plt.Rectangle(*coords, fill=False, edgecolor=color, linewidth=2))
# #currentAxis.text(xmin, ymin, display_txt, bbox={'facecolor':color, 'alpha':0.5})            print label_name,score,xmin,ymin,xmax,ymax
# fileStr0 = img_path.split('.')[-2]
# fileStr0 = fileStr0.split('/')[-1]
# if label_name == 'Person':
# fileStr = '%s/Person5/%s.%d.jpg' %(oPath,fileStr0,i0+1)
# im = img0[ymin:ymax,xmin:xmax]
# r = cv2.imwrite(fileStr,im)
# print 'Person0',fileStr
# if label_name == 'Car1' or label_name == 'Motorbike1':
# fileStr = '%s/Car/%s.%d.jpg' %(oPath,fileStr0,i0+1)
# im = img0[ymin:ymax,xmin:xmax]
# r = cv2.imwrite(fileStr,im)
# print 'Car0',fileStr
# #plt.show()
# #cv2.imshow('im', im)
# #cv2.waitKey(0) if __name__ == "__main__":    img_path = 'test02.jpg'
# mPath = '/media/kingstar/kingstardata/safety_eyes/baidu5'
# oPath = '/media/kingstar/kingstardata/safety_eyes/out'
# trainFileList = listdir(mPath)
# m =len(trainFileList)
# print m
# for i in range(m):
# fileNameStr = trainFileList[i]
# fileStr = fileNameStr.split('.')[-2]
# print i,fileNameStr,fileStr
#      fileNameStr = '%s/%s' % (mPath,fileNameStr)
# print 'step:%d/%d' % (i,m)
# ssd(fileNameStr)