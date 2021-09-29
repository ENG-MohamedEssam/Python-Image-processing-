import cv2

cap = cv2.VideoCapture(1) # default webcam
cap.set(3,640) # 3 for width and then num we want
cap.set(4,480) # 4 for hight and then num we want
cap.set(10,100) #10 for brightness and then the num we want

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if (cv2.waitKey(1) & 0xFF ==ord('q')): # to stop it when pressing q
        break
