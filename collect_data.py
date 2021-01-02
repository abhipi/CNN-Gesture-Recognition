import numpy as np
import cv2 as cv
import os
import time as t


cap = cv.VideoCapture(0)

def captureImage():
    _,frame = cap.read()
    frame = cv.flip(frame, 1)
    frame = cv.rectangle(frame, (340, 10), (590, 260),(255,0,0), 2)

    crop = frame[10:260, 340:590]
    crop = cv.cvtColor(crop,cv.COLOR_BGR2GRAY)
    _,crop = cv.threshold(crop, 115, 255, cv.THRESH_BINARY)

    k = cv.waitKey(27) & 0xFF

    cv.imshow("Crop",crop)
    cv.imshow("Window",frame)

    return k,crop

    

while True:
    k,crop = captureImage()
    
    if k == ord('q'):
        print("Exiting from code")
        break
    if k == ord('r'):
        print("Started Creating Dataset")
        imgn = input('Enter gesture name i.e (0,1,2 or A,B,C):')
        testfolder = "./data/test/"+imgn
        os.makedirs(testfolder)
        
        trainfolder = "./data/train/"+imgn
        os.makedirs(trainfolder)

        for x in range(10):
            k,crop = captureImage()
            crop = cv.resize(crop, (64,64))
            imgName = testfolder +"/"+str(x)+".png" 
            cv.imwrite(imgName,crop)
            print(imgName)
            t.sleep(1)
            
        for x in range(100):
            k,crop = captureImage()
            crop = cv.resize(crop, (64,64))
            imgName = trainfolder +"/"+str(x)+".png" 
            cv.imwrite(imgName,crop)
            print(imgName)
            t.sleep(1)
            
    
    

cap.release()
cv.destroyAllWindows()
