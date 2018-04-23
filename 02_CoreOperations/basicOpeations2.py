import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
# 添加边框
blue = [255, 0, 0]
img1 = cv.imread('F:/OpenCV/python/CoreOperations/logo.jpg')
replicate = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_REPLICATE)
reflect = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_REFLECT)
reflect101 = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_REFLECT_101)
wrap = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_WRAP)
constant = cv.copyMakeBorder(img1, 10, 10, 10, 10, cv.BORDER_CONSTANT, value=blue)

plt.subplot(231),plt.imshow(img1, 'gray'), plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate, 'gray'), plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect, 'gray'), plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101, 'gray'), plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(img1, 'gray'), plt.title('WRAP')
plt.subplot(236),plt.imshow(constant, 'gray'), plt.title('CONSTANT')
plt.show()