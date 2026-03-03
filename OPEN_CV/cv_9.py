# GAUSSIAN BLUR
import cv2

img = cv2.imread("D:/CODING VS CODE/PYCHARM/OPEN_CV/1.1.png")

# resized = cv2.resize(img,(640,640))

# ksize = (7, 7)
# sigmax = 0
# sigmay = 0

# blur = cv2.GaussianBlur(resized, ksize,sigmax)

# cv2.imshow('Input', resized)
# cv2.imshow('Output', blur)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# MEDIAN BLUR
resize = cv2.resize(img,(520,520))

kernel = 3

blur = cv2.medianBlur(resize, kernel)

cv2.imshow('Input', resize)
cv2.imshow('output', blur)

cv2.waitKey(0)
cv2.destroyAllWindows()