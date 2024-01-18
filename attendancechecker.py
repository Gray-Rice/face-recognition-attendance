import cv2
import csv
import imagecapture
import face_recognition
import time

"""
this module is used when we need to check attendace
when called it calls the image capture module and takes an image of the student
it then matches this image with every image in the database and if any match is found
it prints welcome student along with their name
additionally when a student logs in their attendance, their name along with the time and 
date they logged in will get stored into the attendace.csv file
"""

def userlogin():
    img = imagecapture.imageCapture()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    f = open("UserInfo.csv", "r")
    readerObj = list(csv.reader(f))

    oldUser_face_encodings = face_recognition.face_encodings(img)[0]   # reads the facial features of the input image and stores it into a variable
                                                                       # these encodings are then used to match with the face encodings of the stored image in the 
                                                                       # database
    f = open("Attendance.csv", "a")
    reader = csv.writer(f)

    for i in readerObj:
        try:
            img2  = face_recognition.load_image_file("database/USER_ID_{}.png".format(i[-1]))
            img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
            face_enc = face_recognition.face_encodings(img2)[0]  # reads the face encodings of the image in the database
            if face_recognition.compare_faces([oldUser_face_encodings],face_enc):  # compare_faces compares the face encodings of the image in database and the input image
                                                                                   # if they match or are similar then it returns true 
                # below code gets the system date and time at the time of login
                year,month,day,hour,min,sec = time.localtime()[0:6]
                date = "{}-{}-{}".format(year, month, day)
                time1 = "{}hrs-{}mins-{}secs".format(hour, min, sec)
                reader.writerow([date, time1, i[0]]) # stores login information

                output = "Welcome"+ i[0]
                break
        except:
            continue
    else:
        output = "Not recognised"
    f.close()
    return output    
