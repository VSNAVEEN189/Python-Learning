# READING A VIDEO
import cv2

video = cv2.VideoCapture("D:/CODING VS CODE/PYCHARM/OPEN_CV/nature.mp4")

while video.isOpened():

    _,frame = video.read()
    frame = cv2.resize(frame, (800,720))

    cv2.imshow('Output', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
     break
cv2.destroyAllWindows()



# WRITING A VIDEO
fourcc = cv2.VideoWriter_fourcc(*'mp4v')       #Helps the video to compress
output = cv2.VideoWriter('Output.mp4',fourcc,50.0,(1920,1080))

while video.isOpened():
    ret, frame = video.read()
    if ret:
        output.write(frame)
        cv2.imshow('Frame', frame)

        if cv2.waitKey(10) == ord('s'):
            break
    else:
        break

cv2.destroyAllWindows()