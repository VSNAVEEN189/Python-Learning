# SCALING UP AND DOWN
import cv2

img = cv2.imread("D:/CODING VS CODE/PYCHARM/OPEN_CV/1.1.png")

print("Dimensions of Original image: ", img.shape)

scale = 50

width = int(img.shape[1]*scale / 100)
height = int(img.shape[0]*scale / 100)

dim = (width, height)

resized = cv2.resize(img, dim, interpolation=cv2.INTER_LINEAR)   
print("Dimensions of resized image: ", resized.shape)

cv2.imshow('Rezised', resized)
cv2.imshow('Original', img)

cv2.waitKey(0)
cv2.destroyAllWindows()