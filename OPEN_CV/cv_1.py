# Reading an image
import cv2

img = cv2.imread("C:/Users/VICTUS/OneDrive - K L University/Pictures/Ai automation/1.1.png")  #Argument 0 shows the image in greyscale format

cv2.imshow("window", img)

cv2.waitKey(0)           #Shows the waiting time number inside it is in milliseconds

cv2.destroyAllWindows()  #Only the window should be open all other has to be closed


# Writing an image(Saving)
img = cv2.imread("C:/Users/VICTUS/OneDrive - K L University/Pictures/Ai automation/1.1.png", 0)  

cv2.imshow("window", img)

cv2.imwrite("D:/CODING VS CODE/PYCHARM/OPEN_CV/GK.png", img)

cv2.waitKey(0)           

cv2.destroyAllWindows() 


# Resizing an image

img = cv2.imread("C:/Users/VICTUS/OneDrive - K L University/Pictures/Ai automation/1.1.png", 0)  

print("Dimension of the image: " , img.shape)

width = img.shape[1]
height = 400
dim = (width,height)
resized = cv2.resize(img, dim)

cv2.imshow("window", resized)

cv2.waitKey(0)           

cv2.destroyAllWindows() 
