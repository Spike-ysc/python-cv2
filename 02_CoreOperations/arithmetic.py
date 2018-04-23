import cv2 as cv
# 两个图片合并
img1 = cv.imread('F:/OpenCV/python/CoreOperations/demo2.jpg')
img2 = cv.imread('F:/OpenCV/python/CoreOperations/logo.jpg')
# 这里必须是同样大小的,不然会出错
# dst = cv.addWeighted(img1, 0.7, img2, 0.3, 0)

rows, cols, channels = img2.shape
# 在img1中裁剪出和img2等大小的图片
roi = img1[0:rows, 0:cols]
# 灰度化处理
img2Gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
# 阈值滤波
ret, mask = cv.threshold(img2Gray, 10, 255, cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)

img1_bg = cv.bitwise_and(roi, roi, mask = mask_inv)
img2_fg = cv.bitwise_and(img2, img2, mask = mask)

dst = cv.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst
cv.imshow('res', img1)
cv.waitKey(0)
cv.destroyAllWindows()