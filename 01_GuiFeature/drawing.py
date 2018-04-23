import numpy as np
import cv2 as cv

img = np.zeros((512, 512, 3), np.uint8)

# 线段
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
# 长方形
cv.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
# 圆形
cv.circle(img, (455, 63), 63, (0,0,255), -1)
# 椭圆
cv.ellipse(img, (255, 256), (100, 50), 0, 0, 180, 255, -1)
# 画线
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv.polylines(img, [pts], True, (0, 255, 255))
# 添加文字
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img, 'OpenCV', (10, 500), font, 4, (255,255,255), 2, cv.LINE_AA)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()