# -*- coding:utf-8 -*-

import numpy as np
import cv2 as cv

img = cv.imread('F:/OpenCV/python/CoreOperations/demo2.jpg', -1)
# cv.imshow('image', img)
# cv.waitKey(0)
# cv.destroyAllWindows()
px = img [100, 100]
print('根据图片行和列坐标访问像素值')
print('img[100,100]的像素值是:',px)
blue = img [100, 100, 0]
print('只访问蓝色像素为:', blue)
print('更好的像素访问和编辑方法')
print('行坐标和列坐标为10, 10, 通道为2的像素为:',img.item(10, 10, 2))
img.itemset((10, 10, 2), 100)
print('img.item(10,10,2)的像素已经修改为:', img.item(10, 10, 2))
print('图片的形状,(行, 列, 通道数)', img.shape)
print('图片的总像素数:',img.size)
print('图片数据类型', img.dtype)
