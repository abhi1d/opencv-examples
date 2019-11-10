import cv2
import numpy as np
# img = cv2.imread('lena.jpg', -1)
img = np.zeros([1000, 1000, 3], np.uint8)

img = cv2.line(img, (0,0), (255,255), (92, 184, 133), 5)
img = cv2.arrowedLine(img, (255,0), (255,255), (255, 0, 0), 5)

img = cv2.rectangle(img, (384, 0), (510, 120), (0, 0, 255), 10)
img = cv2.circle(img, (400, 400), 20, (0,255,0), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'Open CV', (233,500), font, 4, (130,130,130), 10, cv2.LINE_AA)

cv2.imshow('image', img)
k = cv2.waitKey(0)
