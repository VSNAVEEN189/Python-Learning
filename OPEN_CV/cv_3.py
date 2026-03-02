import cv2

img = cv2.imread("D:/CODING VS CODE/PYCHARM/OPEN_CV/1.1.png")
width = 600
height = 850
dim = (width, height)

resized = cv2.resize(img, dim)
print('Size in bytes: ' , img.size)    # Checks the size of an image in the form of bytes

cv2.imshow("Original", resized)

flip = cv2.flip(resized,1)  # 1 means flipping horizontally
cv2.imshow('Horizontal', flip)

flip_1 = cv2.flip(resized,0)    # 0 means flipping vertically 
cv2.imshow('Vertical', flip_1)

flip_2 = cv2.flip(resized, -1)
cv2.imshow('Horizontal & Vertical', flip_2)  # -1 both horizontally and vertically

cv2.waitKey(0)
cv2.destroyAllWindows()