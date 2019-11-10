import cv2

img = cv2.imread('lena.jpg', -1)

print(img)

cv2.imshow('image', img)
k = cv2.waitKey(0)
