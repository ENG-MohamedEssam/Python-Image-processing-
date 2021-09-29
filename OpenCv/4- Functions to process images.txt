import cv2
import numpy as np #importing the library for calculations

img = cv2.imread("D:/Deep Learning/OpenCv/1.jpg") # to read the image
kernel = np.ones((5,5),np.uint8) #all numbers are ones , unsigned integer so the values will range from 0 to 255
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # to make it Gray
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) # to make it blur
imgCanny = cv2.Canny(img,150,200) # to detect edges nums for threshold
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1) # iterations define the thickness of dialation
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Gray Image",imgGray) # to show the gray image
cv2.imshow("Gray Blur Image",imgBlur)   # to show the blurred gray image
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0) # to delay
