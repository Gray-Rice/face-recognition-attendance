import cv2
import imagecapture
import newstudent
import attendancechecker
import os
import csv
import face_recognition
import numpy

print("----------------------------------------------")
print("                  WELCOME")
print("ATTENDANCE OR NEW STUDENT?  (0/1)")

input_status = int(input(">>>"))

if input_status == 1:
    znewstudent.new_student()
elif input_status == 0:
    zzattendancechecker.oldUserLogin()
