import cv2
import numpy as np

faceCascade = cv2.CascadeClassifier("D:/Deep Learning/OpenCv/opencv-master/data/haarcascades/haarcascade_frontalface_default.xml") # cascade given by opencv
img = cv2.imread('D:/Deep Learning/OpenCv/1.jpg')
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) # put a rectange on the image
cv2.imshow("Result",img)

# we can use already made cascades by people or we can make our own to detect cars tvs ect ...
#cascade is an old algorithm but it works fast and well in certain circumstances
cv2.waitKey(0)
