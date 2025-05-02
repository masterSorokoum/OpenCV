import cv2
import numpy as np

img = cv2.imread("redcircle.png", 1)           # -1 - фальфа канал; 0 - черно/белое; 1 - белый фон
cv2.namedWindow("Result", cv2.WINDOW_NORMAL)   #позволяет растягивать окно 
cv2.imshow("Result", img)                      #публикуем изображение 
cv2.waitKey(0)                                 #ждем нажатие любой клавиши
cv2.destroyAllWindows                          #закрываем все окна 
