import cv2
print("Package Imported")
#pic cap
img = cv2.imread("D:/Deep Learning/OpenCv/1.jpg") # read the pic
cv2.imshow("My pic", img) # show the img
cv2.waitKey(0) # wait and stop bec of 0
