import numpy as np
import cv2 as cv

im = cv.imread('F:/OpenCV/python-cv2/python-cv2/03_imageProcessing/heibai.jpg')
imgray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
ret, thresh = cv.threshold(imgray, 127, 255, 0)
im2, contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

im3 = cv.drawContours(im2, contours, -1,(0, 255,0), 3)
cv.imshow('img',im)
cv.imshow('img1', im3)
# cv.imshow('img2', hierarchy)
cv.waitKey(0)
cv.destroyAllWindows()