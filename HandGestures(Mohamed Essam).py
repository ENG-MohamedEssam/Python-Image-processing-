import cv2
import time
import os
import HandTrackingModule as htm

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0+cv2.CAP_DSHOW) # to capture live feed
cap.set(3, wCam) # width
cap.set(4, hCam) #Height

folderPath = "D:/Deep Learning/OpenCv/Finger Images" # folder path for images
myList = os.listdir(folderPath) # list the images
print(myList) # print the list of images
overLayList = [] # list of images if i want first one overLayList[0]
for imPath in myList :
    image = cv2.imread(f'{folderPath}/{imPath}') # read images in the folder path
    overLayList.append(image) # saving the images in a list

print(len(overLayList)) # if the length is 6 we're good to go
pTime = 0 #initalize previous time
detector = htm.handDetector(detectionCon = 8.75) # hand detector
tipIds = [4, 8, 12, 16, 20] #fingers tips

while True : # loop for capturing frames
    success, img = cap.read() # To capture frames
    img = detector.findHands(img) # return img back
    lmList = detector.findPosition(img, draw=False)# track the position of the hand
    #print(lmList) # to see if we get something

    if len(lmList) != 0:
        fingers = []
        #if lmList[8][2] < lmList[6][2]  # from pic on mediapipe site
        #thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]: # check only 1 value below
            fingers.append(1)  # if finger is open append 1
        else:
            fingers.append(0)  # if finger is closed append 0

        for id in range(1,5): # for the four fingers
            #four fingers
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2] :
                fingers.append(1) # if finger is open append 1
            else :
                fingers.append(0) # if finger is closed append 0

        #print(fingers)
        totalFingers = fingers.count(1)
        print(totalFingers)


        h, w, c = overLayList[totalFingers-1].shape # this makes us not worry about height and width of images
        img[0:h, 0:w] = overLayList[totalFingers-1] # where to display the image
        # if we put -1 in a list in python it'll take the last element of the list
        cv2.rectangle(img, (28,255),(178,425),(0,255,0),cv2.FILLED) # put a green rectangle
        cv2.putText(img, str(totalFingers),(45,375),cv2.FONT_HERSHEY_PLAIN,
                    18,(255,0,0),25)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime # to update previous value every loop
    cv2.putText(img, f'FPS: {int(fps)}',(420,50), cv2.FONT_HERSHEY_PLAIN,
                3,(255,0,0),3) # where to put the text and it's font and color

    cv2.imshow("Image", img)
    cv2.waitKey(1)
