import numpy as np
import cv2
import os

path = './photos'
face_cascade = cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')
img = cv2.imread("beards.jpg")
if not face_cascade.empty():
    if img is not None:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        i = 0
        for (x,y,w,h) in faces:
            crop_img = img[y:y+h, x:x+w]
            cv2.imwrite( os.path.join(path, str(i+1) + '.png') ,cv2.resize(crop_img, (50, 50)))