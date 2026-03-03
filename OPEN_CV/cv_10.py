# BILATERAL FILTER
import cv2

img = cv2.imread("D:/CODING VS CODE/PYCHARM/OPEN_CV/bird.jpeg")

resize = cv2.resize(img,(520,700))

d = 7
sigmacolor = 100
sigmaspace = 100

b = cv2.bilateralFilter(img,d,sigmacolor,sigmaspace)

cv2.imshow('Input', resize)
cv2.imshow('Output', b)

cv2.waitKey(0)
cv2.destroyAllWindows()