import cv2
import numpy as np #importing the library for calculations

img = cv2.imread("D:/Deep Learning/OpenCv/cards.jpg")

imghor = np.hstack((img,img)) # stack images horizontally ( numpy func )
imgVer = np.vstack((img,img)) # stack images Vertically

cv2.imshow("Horizontal",imghor)
cv2.imshow("Vertical",imgVer)


cv2.waitKey(0)

#note , he wrote a fuction to scale the stacked images don't forget to look it up
