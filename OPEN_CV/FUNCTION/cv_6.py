#SHIFTING OF AN IMAGE
import cv2
import numpy as np 

img = cv2.imread("D:/CODING VS CODE/PYCHARM/OPEN_CV/1.1.png")

column = img.shape[1]
row = img.shape[0]

x = np.float32([(1,0,150),(0,1,70)])
         #width to right, down width

shifted = cv2.warpAffine(img,x,(column,row))

cv2.imshow('Original Image', img)
cv2.imshow('Shifted Image', shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()