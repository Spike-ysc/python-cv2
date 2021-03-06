import numpy as np
import cv2 as cv

def draw_circle(event, x, y, flags, param):
    # 监听鼠标双击
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img, (x, y), 100, (255, 0, 0), -1)

img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)

while(1):
    cv.imshow('image', img)
    if cv.waitKey(20) & 0xff == 27:
        break
cv.destroyAllWindows()