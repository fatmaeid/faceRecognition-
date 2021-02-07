import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = "AttendenceImages"
images = []
classNames = []

myList = os.listdir(path)
for cls in myList:
    image = cv2.imread(f'{path}/{cls}')
    images.append(image)
    classNames.append(os.path.splitext(cls)[0])

# encoding all the images
def findEncoding(images):
    encodingList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encodeingImg = face_recognition.face_encodings(img)[0]
        encodingList.append(encodeingImg)
    return encodingList

def markAttendence(name):
    with open('Attendence.csv','r+') as f:
        nameList = []
        myDataList = f.readlines()
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')


EncodeListKnown = findEncoding(images)

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgs = cv2.resize(img,(0,0),None,0.25,0.25)
    imgs = cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgs)
    encodesCurFrame = face_recognition.face_encodings(imgs,facesCurFrame)

    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(EncodeListKnown,encodeFace)
        facesDis = face_recognition.face_distance(EncodeListKnown,encodeFace)

        matchIndex = np.argmin(facesDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0))
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 0, 255), cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendence(name)

    cv2.imshow("Frame",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()