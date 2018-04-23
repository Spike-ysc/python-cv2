# 边缘检测
import cv2
import numpy as np
from matplotlib import pyplot as plt

def nothing(x):
    pass

# img = cv2.imread('che.jpg')
img = cv2.imread('ceshi2.bmp')

cv2.namedWindow('image')

cv2.createTrackbar('Val','image',0,500,nothing)


while(1):
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    Val = cv2.getTrackbarPos('Val','image')

   
    edges = cv2.Canny(img, Val,Val+100 )

    cv2.imshow('image',edges)
cv2.destroyAllWindows()

# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

# plt.show()