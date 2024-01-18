from newstudent import new_student
from attendancechecker import userlogin

import tkinter as tk
from tkinter import simpledialog, messagebox

def newstu():
    user_input = simpledialog.askstring("Input", "Enter Name:")
    output = new_student(user_input)
    messagebox.showinfo("New Student", output)
    return

def oldstu():
    output = userlogin()
    messagebox.showinfo("Old Student", output)
    return

# Create main window
root = tk.Tk()
root.title("Attendance")

# Create buttons for options
button1 = tk.Button(root, text="New Student", command=newstu)
button2 = tk.Button(root, text="Existing Student", command=oldstu)

# Place buttons in the window
button1.pack(pady=10)
button2.pack(pady=10)

# Start the main loop
root.mainloop()