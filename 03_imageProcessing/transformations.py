# -*- coding:utf-8 -*-
# 图像旋转处理
import cv2 as cv
import numpy as np

img = cv.imread('F:/OpenCV/python/CoreOperations/demo2.jpg', 0)
rows, cols = img.shape

pts1 = np.float32([[50,50], [200, 50], [50, 200]])
pts2 = np.float32([[10,100], [200, 50], [100, 250]])

M = np.float32([[1, 0, 100], [0, 1, 50]])
M2 =cv.getRotationMatrix2D(((cols-1)/2.0, (rows-1)/2.0), 90, 1)
M3 = cv.getAffineTransform(pts1, pts2)

dst = cv.warpAffine(img, M, (cols, rows))
dst2 = cv.warpAffine(img, M2, (cols, rows))
dst3 = cv.warpAffine(img, M3, (cols, rows))

cv.imshow('移动', dst)
cv.imshow('旋转', dst2)
cv.imshow('3d旋转', dst3)
cv.waitKey(0)
cv.destroyAllWindows()