import numpy as np
import cv2 as cv

def nothing(x):
    pass

img = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')
# 第一个参数是trackbar名称，
# 第二个参数是它所连接的窗口名称，
# 第三个参数是默认值，
# 第四个参数是最大值，
# 第五个参数是执行的回调函数每次trackbar值都会发生变化。
# 回调函数总是有一个默认参数，它是trackbar的位置。在
# 我们的例子中，函数什么都不做，所以我们只是通过。
cv.createTrackbar('R', 'image', 0, 255, nothing)
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('B', 'image', 0, 255, nothing)

# 轨道条还可以作为开关
switch = '0: OFF \n 1:ON'
cv.createTrackbar(switch, 'image', 0, 1, nothing)

while(1):
    cv.imshow('image', img)
    k = cv.waitKey(1) & 0xff
    if k == 27:
        break
    # 获取进度条的值
    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]
cv.destroyAllWindows()