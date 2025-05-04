import cv2
import numpy as np

cv2.namedWindow('HSV')      # окно настроек HSV
cv2.namedWindow('Result')   # окно с изображением

img = cv2.imread('circle.png') #читаем изображение 
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 

def callback(x):
    pass
cv2.createTrackbar('h1', 'HSV', 0, 255, callback)
cv2.createTrackbar('s1', 'HSV', 0, 255, callback)
cv2.createTrackbar('v1', 'HSV', 0, 255, callback)
cv2.createTrackbar('h2', 'HSV', 179, 179, callback)
cv2.createTrackbar('s2', 'HSV', 255, 255, callback)
cv2.createTrackbar('v2', 'HSV', 255, 255, callback)

while True:
    h1 = cv2.getTrackbarPos('h1', 'HSV')
    s1 = cv2.getTrackbarPos('s1', 'HSV')
    v1 = cv2.getTrackbarPos('v1', 'HSV')
    h2 = cv2.getTrackbarPos('h2', 'HSV')
    s2 = cv2.getTrackbarPos('s2', 'HSV')
    v2 = cv2.getTrackbarPos('v2', 'HSV')

    hsv_min = np.array([h1, s1, v1], dtype=np.uint8)
    hsv_max = np.array([h2, s2, v2], dtype=np.uint8)

    filter_color = cv2.inRange(hsv, hsv_min, hsv_max)

    cv2.imshow('Result', filter_color)

    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC для выхода
        break

cv2.destroyAllWindows()
