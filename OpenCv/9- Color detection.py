import cv2
import numpy as np

def empty(a): # it does nothing
    pass
path = "D:/Deep Learning/OpenCv/cards.jpg"
cv2.namedWindow("TrackBars") # creating new window by the name track bars
cv2.resizeWindow("TrackBars",640,240) # initialize window for resizing ( must be the same name )
cv2.createTrackbar("Hue Min","TrackBars",0,179,empty)# min val 0 max val 179 in opencv , we have to call the function to be called everytime the user changes the value on track bar
cv2.createTrackbar("Hue Max","TrackBars",179,179,empty)
cv2.createTrackbar("Sat Min","TrackBars",70,255,empty)
cv2.createTrackbar("Sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("Val Min","TrackBars",84,255,empty)
cv2.createTrackbar("Val Max","TrackBars",255,255,empty)
# took the values then worte them as the first number then we got the mask
while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max","TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper) # it will give us the filtered out image of the color
    imgResult = cv2.bitwise_and(img,img,mask=mask) #take the filtered image with its color


    cv2.imshow("Image",img)
    cv2.imshow("Hsv",imgHSV)
    cv2.imshow("MASK", mask)
    cv2.imshow("Result", imgResult)
    cv2.waitKey(1)

    #keep the color that we don't want in black and what we need in white
    # we can also use the stack function for stacking all the images ( function is in his code )
