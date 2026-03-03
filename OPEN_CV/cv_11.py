# EDGE DETECTION
import cv2
import numpy as np

img = cv2.imread("D:/CODING VS CODE/PYCHARM/OPEN_CV/bird.jpeg")
resize = cv2.resize(img,(520,520))
min_thresh = 100   #Below 100 Converts to black   
max_thresh = 200   #Above 200 Converts to white 
edges = cv2.Canny(resize,min_thresh,max_thresh)

cv2.imshow('Original', resize)
cv2.imshow('Edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()