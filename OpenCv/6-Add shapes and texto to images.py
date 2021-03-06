import cv2
import numpy as np #importing the library for calculations

img = np.zeros((512,512,3),np.uint8) # image 512 x 512 x 3 and has values from 0 to 255
#print(img)
#img[200:300,100:300] = 255,0,0 # blue for the specified range
#img[:] = 255,0,0 # blue for the whole image

#cv2.line(img,(0,0),(300,300),(0,255,0),3) # green line starts from (0,0) and goes to (300,300)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3) # width and hight using shape func
#shape matrix has 3 elements hight,width and channels
cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED) # cv2.fill for filling the rectangle
cv2.circle(img,(400,50),30,(255,255,0),5) #(400,50) for center 30 for radius then color then 5 for thickness
cv2.putText(img, "OpenCV ",(300,200),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,200),2) # place then font then scale then color then thickness

cv2.imshow("Image",img)

cv2.waitKey(0)
