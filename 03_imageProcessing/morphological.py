# 侵蚀和扩张等

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('zi.jpg', 0)
kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

plt.subplot(231),plt.imshow(img),plt.title('img')
plt.xticks([]), plt.yticks([])
plt.subplot(232),plt.imshow(erosion),plt.title('erosion')
plt.xticks([]), plt.yticks([])
plt.subplot(233),plt.imshow(dilation),plt.title('dilation')
plt.xticks([]), plt.yticks([])
plt.subplot(234),plt.imshow(gradient),plt.title('gradient')
plt.xticks([]), plt.yticks([])
plt.subplot(235),plt.imshow(tophat),plt.title('tophat')
plt.xticks([]), plt.yticks([])
plt.subplot(236),plt.imshow(opening),plt.title('opening')
plt.xticks([]), plt.yticks([])
plt.show()