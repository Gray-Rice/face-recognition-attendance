import cv2
import imagecapture
import os
import csv
import face_recognition
import numpy
from imagecapture import imageCapture

def new_student(new_student_name):
    if new_student_name == " " or new_student_name == None:
        return "Enter valid name"
    
    f = open("UserInfo.csv", "r")
    data =  list(csv.reader(f))
    
    if not(data == None):
            for x in data:
                if x[0] == new_student_name:
                    return "Student already exists"
    

    if " " in new_student_name:
        name = ""
        for x in new_student_name.split(" "):
            name = name + str(x.capitalize)
        new_student_name = name
    else:
        new_student_name = new_student_name.capitalize()

    new_student_img = imageCapture()
    
    if len(data)>1:
        student_user_id = int(data[-1][1])+1
    else:
        student_user_id = 1
    
    f = open("UserInfo.csv", "a+")

    writerObj = csv.writer(f)
    ls = [new_student_name, student_user_id]
    writerObj.writerow(ls)

    os.rename("Image.png", f"database/USER_ID_{student_user_id}.png")

    f.close()
    return f"Student {new_student_name} added succesfully"
