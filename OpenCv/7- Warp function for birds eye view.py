import cv2
import numpy as np #importing the library for calculations

img = cv2.imread("D:/Deep Learning/OpenCv/cards.jpg")
width,height = 250,350 # normal card dims
pts1 = np.float32([[138,27],[218,62],[89,166],[172,199]]) # four corner points of a card
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2) # matrix taking points
imgOutput = cv2.warpPerspective(img,matrix,(width,height)) #warp funcrion , define source and matrix and width and height

cv2.imshow("Image",img)
cv2.imshow("Op",imgOutput)

cv2.waitKey(0)
