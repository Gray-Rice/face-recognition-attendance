import cv2
import numpy as np
import face_recognition
from PIL import Image
import os

img1 = cv2.imread("Test.png")
img2 = cv2.imread("testimg.jpg")

img1enc = face_recognition.face_encodings(img1)[0]
img2enc = face_recognition.face_encodings(img2)[0]

recognizer = face_recognition.compare_faces([img1enc], img2enc)

if recognizer[0] == True:
    print("Welcome!")
else:
    print("Please try again!")