# 图像金字塔放大缩小图像、合并图像

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('timg.jpg')
# 缩小为原来的1/4
lower_reso = cv2.pyrDown(img)
# 放大为原来的4倍
higher_reso = cv2.pyrUp(lower_reso)

cv2.imshow('img', img)
cv2.imshow('lower_reso', lower_reso)
cv2.imshow('higher_reso', higher_reso)
cv2.waitKey(0)
cv2.destroyAllWindows()