import numpy as np
import cv2 as cv
from keras.models import model_from_json
import operator
import sys
import os

json_file=open("./model-bw.json","r")
model_json=json_file.read()
json_file.close()

loaded_model=model_from_json(model_json)

loaded_model.load_weights("./model-bw.h5")

print("Model loading is completed!!!")

categories=["ZERO", "ONE", "TWO","THREE", "FOUR", "FIVE"]

cap=cv.VideoCapture(0)

def captureImage():
    while True:
        ret,frame=cap.read()
        frame=cv.flip(frame,1)
        frame = cv.rectangle(frame, (340, 10), (590, 260),(255,0,0), 2)

        crop = frame[10:260, 340:590]
        crop = cv.cvtColor(crop,cv.COLOR_BGR2GRAY)
        _,crop = cv.threshold(crop, 115, 255, cv.THRESH_BINARY)

        k = cv.waitKey(27) & 0xFF

        cv.imshow("Crop",crop)
        cv.imshow("Window",frame)

        return k,crop

while True:
    k,crop=captureImage()
    crop=cv.resize(crop, (64,64))
    result=loaded_model.predict(crop.reshape(1,64,64,1))
    res=list(result[0])
    res=list(map(int,res))
    for i in range(len(res)):
        if(res[i]==1):
            print(categories[i])

    if(k==ord('q')):
        break
    
cap.release()
cv.destroyAllWindows
