import subprocess
import user_manager
from tkinter import *
import os


root = Tk()
root.title('New Analyzer')

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

frame1 = LabelFrame(root)
frame1.pack()
myLabel1 = Label(frame1, text="User Login", font=("Arial", 25))
myLabel1.grid(row=0, column=0)

frame2 = LabelFrame(root)
frame2.pack()

username = Label(frame2, text="Username: ")
password = Label(frame2, text="Password: ")
input_username = Entry(frame2, width=30)
input_password = Entry(frame2, width=30)

username.grid(row=0, column=0)
password.grid(row=1, column=0)
input_username.grid(row=0, column=1)
input_password.grid(row=1, column=1)

def onClick(window):
    user = user_manager.get(input_username.get(), input_password.get())
    if user is None:
        myLabel = Label(root, text="No User Found")
        myLabel.pack()
    else:
        window.destroy()
        os.system("python News_sources_codes/home_gui.py")
        
mybutton = Button(root, text="Login", command=lambda:onClick(root))
mybutton.pack()

root.mainloop()
