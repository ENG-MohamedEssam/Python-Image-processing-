import cv2
import numpy as np

def getContours(img): #function to find contours
    contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) # retr external for getting the outer countours to find outer corners , we will get all contours
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 500: # 500 pixels this deleted the things we didn't need like the outer borders of the whole pic
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),2) # draw the contour to see it clearly (put it on imgcontour , give it contour itself , -1 for all contours , color , thickness
            peri = cv2.arcLength(cnt,True) # get the arc length of the contours ( contour parameter )
            print(peri)
            approx = cv2.approxPolyDP(cnt,0.02*peri,True) # How many corner points we have true for closed
            print(len(approx)) # print length of corners
            objCor = len(approx) # object corners
            x,y,w,h = cv2.boundingRect(approx) # create a bounding box arround the object ( get x , y , width and height)

            if objCor ==3: objectType = "Tri" # if it has 3 corners it's a triangle
            elif objCor == 4:
                aspRatio = w/float(h) #define hight as float and divide width and height
                if aspRatio > 0.95 and aspRatio < 1.05: objectType = "sqare" #deviation of 5% for error
                else : objectType = "rectangle"
            elif objCor > 4 : objectType = "Circle"
            else : objectType="None"
            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2) # draw the bounding box on the image contour , point 1 point 2 , colour , thickness
            cv2.putText(imgContour,objectType,
                        (x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,
                        (0,0,0),1) # where to put the text

path = 'D:/Deep Learning/OpenCv/shapes.PNG'
img = cv2.imread(path)
imgContour = img.copy() # making a copy of the original image to put the contours on


imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),1)
imgCanny = cv2.Canny(imgBlur,50,50)
getContours(imgCanny)
imgBlank = np.zeros_like(img)

cv2.imshow("Image",img)
cv2.imshow("Gray",imgGray)
cv2.imshow("Blur",imgBlur)
cv2.imshow("Canny",imgCanny)
cv2.imshow("Blank",imgBlank)
cv2.imshow("Contour",imgContour)

cv2.waitKey(0)
# we can also use the stack function
