# 寻找图像渐变，边缘
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('che.jpg',0)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel = cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=3)

cv2.imshow('img', img)
cv2.imshow('laplaction', laplacian)
# cv2.imshow('soblex', sobelx)
cv2.imshow('soble', sobel)
cv2.waitKey(0)
cv2.destroyAllWindows()
# plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
# plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
# plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,4),plt.imshow(sobel,cmap = 'gray')
# plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

# plt.show()