import numpy as np
import cv2
import os
import urllib

path = './photos'
face_cascade = cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')

def getImg(url):
    resp = urllib.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    return image

def getFaces(url):
    image = getImg(url)
    img = cv2.imdecode(image, cv2.IMREAD_COLOR)
    if not face_cascade.empty():
        if img is not None:
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            i = 0
            for (x,y,w,h) in faces:
                crop_img = img[y:y+h, x:x+w]
                cv2.imwrite( os.path.join(path, str(i+1) + '.png') ,cv2.resize(crop_img, (50, 50)))
                
getFaces("https://i.redditmedia.com/hZFAOKryUU2xHST9IxFCGnV0Ct8PITliLSbI6PVFw2k.jpg?w=1024&s=f6fe43bd276beeaeb20a4d646a095bbd")