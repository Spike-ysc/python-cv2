import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('huaban.jpg')
# 卷积模糊
kernel = np.ones((5,5), np.float32)/25
dst = cv2.filter2D(img, -1, kernel)
# 平均滤波
blur = cv2.blur(img, (5,5))
# 高斯滤波
gauss = cv2.GaussianBlur(img, (5,5), 0)
# 中值滤波
media = cv2.medianBlur(img, 5)
# 双边滤波
# 在保持边缘清晰的同时非常有效地去除噪音。但与其他过滤器相比，操作速度较慢
bilatera = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow('img', img)
cv2.imshow('gaussian', gauss)
cv2.imshow('bilatera', bilatera)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.subplot(231),plt.imshow(img),plt.title('Original')
# plt.xticks([]), plt.yticks([])
# plt.subplot(232),plt.imshow(dst),plt.title('Filter2D')
# plt.xticks([]), plt.yticks([])
# plt.subplot(233),plt.imshow(img),plt.title('blur')
# plt.xticks([]), plt.yticks([])
# plt.subplot(234),plt.imshow(dst),plt.title('GaussianBlur')
# plt.xticks([]), plt.yticks([])
# plt.subplot(235),plt.imshow(img),plt.title('medianBlur')
# plt.xticks([]), plt.yticks([])
# plt.subplot(236),plt.imshow(dst),plt.title('bilateralFilter')
# plt.xticks([]), plt.yticks([])
# plt.show()