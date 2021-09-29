import cv2
import numpy as np #importing the library for calculations

img = cv2.imread("D:/Deep Learning/OpenCv/1.jpg")
print(img.shape)

imgResize = cv2.resize(img,(1000, 1000)) #resizing the img by 300 width and 200 hight
print(imgResize.shape) # image after resizing

imgCropped = img[0:200,200:500] # hight first then width (not an opencv func)

cv2.imshow("Image", img)
cv2.imshow("Image Resized", imgResize)
cv2.imshow("Image Cropped", imgCropped)

cv2.waitKey(0)
