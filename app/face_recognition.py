import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from app import models


def getEncoding(image):
    encodeingImg = face_recognition.face_encodings(image)[0]
    return encodeingImg

def file2RGB(file):
    filestr = file.read()
    npimg = np.fromstring(filestr, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def getStudentFromImage(image):
    encodeingImg = getEncoding(image)
    students = models.Student.query.all()
    now = datetime.now()
    
    for student in students:
        enc = np.array(eval(student.face_encoding))
        result = face_recognition.compare_faces([enc], encodeingImg)
        if result[0] == True:
            return student
    return None
