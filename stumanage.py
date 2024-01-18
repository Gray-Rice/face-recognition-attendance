import os
import csv

def remove_student(student_user_id):
    # print("Are you sure you want to delete this record (Press y to countinue, Any other key to exit)")
    c = input().lower()
    if c == "y":
        stu = None
        f = open("UserInfo.csv","r")
        f2 = open("dummy.csv",'w')
        robj = csv.reader(f)
        wobj = csv.writer(f2)
        dat = list(robj)
        for x in dat:
            if int(x[1]) == int(student_user_id):
                stu = x
                os.remove(f"database/USER_ID_{stu[1]}.png")
            else: 
                wobj.writerow(x)
                
        f.close()
        f2.close()
        os.remove("UserInfo.csv")
        os.rename("dummy.csv","UserInfo.csv")
        if stu == None:
            out = "Student not found"
        else:
            out =f"{stu[0]} removed"
        return out

def list_student():
    f = open("UserInfo.csv","r")

