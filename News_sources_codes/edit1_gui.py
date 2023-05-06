from tkinter.ttk import Style
import user_manager
from tkinter import *
from PIL import Image, ImageTk
import news_structure1 as nw1
import news_date as ndate
import news_structure2 as nw2
import os
import news_structure3 as nw3


def load_image(file_path, x, y):
    img = Image.open(file_path)
    new_img = img.resize((x, y))
    photo_img = ImageTk.PhotoImage(new_img)
    return photo_img


root = Tk()
root.title('Main Page')

content_frame = Frame(root)
content_frame.pack()

label = Label(content_frame, text="My Profile", font=('Arial', 20))
label.grid(row=0, column=0, padx=3, pady=3)

profile_img = load_image("Image/male_profile.png", 145, 100)

label_profile = Label(content_frame, image=profile_img, text="", compound="top", highlightthickness=1, highlightbackground="black")

label_profile.grid(row=1, column=0, pady=3, padx=20)

button_upload = Button(content_frame, text="Upload")
button_upload.grid(row=2, column=0, pady=10)

frame_name = Frame(content_frame)
frame_name.grid(row=1, column=1, padx=4, pady=10)

label_name = Label(frame_name, text="Display Name: ", font=('Arial', 12))
label_name.grid(row=0, column=0, padx=40, pady=5)



name = Entry(frame_name, width=25)
name.insert(0, "Alibaba Mohammad Ali Bin")

name.grid(row=1, column=0)



button_save = Button(content_frame, text="Save Changes", foreground='black', background='green', font=('Arial', 12))
button_save.grid(row=2, column=1, padx=10)

root.mainloop()
