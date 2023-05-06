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
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))


# Create a frame to hold the content
content_frame = Frame(root)



# Set the content_frame to expand to fill the window
content_frame.pack(expand=True, fill=BOTH)


# Create a frame with a black background
frame1 = Frame(content_frame, bg="#1C1C1C")
frame1.pack(fill="both", expand=False, side="top")


# Open image
img = Image.open("Image/news_icon.png")

# Resize image
new_img = img.resize((80, 65))

# Convert image to PhotoImage
photo_img = ImageTk.PhotoImage(new_img)

# Create a label and display the image on the frame
label = Label(frame1, image=photo_img, bg="#1C1C1C")

# Create buttons with custom font and colors
font = ("Arial", 12)
bg_color = "#4B4B4B"
fg_color = "#FFFFFF"

def onclick_home(window):
    window.destroy()
    os.system("python News_sources_codes/home_gui.py")

def onclick_trending(window):
    window.destroy()
    os.system("python News_sources_codes/trending_gui.py")

def onclick_sports(window):
    window.destroy()
    os.system("python News_sources_codes/sports_gui.py")

def onlick_entertainment(window):
    window.destroy()
    os.system("python News_sources_codes/entertainment_gui.py")

def onclick_lifestyle(window):
    window.destroy()
    os.system("python News_sources_codes/lifestyle_gui.py")


home_button = Button(frame1, text="Home", font=font, bg=bg_color, fg=fg_color, padx=15, pady=5, width=13, command=lambda:onclick_home(root))
trending_button = Button(frame1, text="Trending", font=font, bg=bg_color, fg=fg_color, padx=15, pady=5, width=13, command=lambda:onclick_trending(root))
sports_button = Button(frame1, text="Sports", font=font, bg=bg_color, fg=fg_color, padx=15, pady=5, width=13, command=lambda:onclick_sports(root))
entertainment_button = Button(frame1, text="Entertainment", font=font, bg=bg_color, fg=fg_color, padx=15, pady=5, width=13, command=lambda:onlick_entertainment(root))
lifestyle_button = Button(frame1, text="Lifestyle", font=font, bg=bg_color, fg=fg_color, padx=15, pady=5, width=13, command=lambda:onclick_lifestyle(root))

# Create a frame for search bar
search_frame = Frame(frame1, padx=15, pady=5)

# Open and resize image
img2 = Image.open("Image/search.png")
new_img2 = img2.resize((20, 20))

# Convert image to PhotoImage
photo_img2 = ImageTk.PhotoImage(new_img2)

# Create search button and entry widget
search_entry = Label(search_frame,text="Search" ,font=font, bd=0, width=20, anchor=W)
#search_entry.insert(0, "Search")
def onclick_search(window):
    window.destroy()
    os.system("python News_sources_codes/search_gui.py")

search_button = Button(search_frame, image=photo_img2, borderwidth=0, activebackground="#1C1C1C", command=lambda:onclick_search(root))
# Define function to perform search


# Open image
img3 = Image.open("Image/profile.png")

# Resize image
new_img3 = img3.resize((80, 65))

# Convert image to PhotoImage
photo_img3 = ImageTk.PhotoImage(new_img3)

# Create a button and display the image on the frame
button3 = Button(frame1, image=photo_img3, bg="#1C1C1C")

# Arrange the elements with spacing and padding
label.grid(row=0, column=0, padx=10, pady=10)

button3.grid(row=0, column=1, padx=50)
home_button.grid(row=0, column=2, padx=15, pady=10)
trending_button.grid(row=0, column=3, padx=15, pady=10)
sports_button.grid(row=0, column=4, padx=15, pady=10)
entertainment_button.grid(row=0, column=5, padx=15, pady=10)
lifestyle_button.grid(row=0, column=6, padx=15, pady=10)
empty_space2 = Label(frame1, bg="#1C1C1C")
empty_space2.grid(row=0, column=7, padx=18)
search_entry.pack(side=LEFT)
search_button.pack(side=LEFT)
search_frame.grid(row=0, column=8, padx=10, pady=10)

 
frame2 = Frame(content_frame)

label_trending = Label(frame2, text="Setting", font=('Arial', 25),)
label_trending.pack()
# Arrange the elements
frame1.grid(row=0, column=0)
frame2.grid(row=1, column=0, columnspan=2, sticky="W", padx=30, pady=10)



frame_content = Frame(content_frame)
frame_content.grid(row=2, column=0)

#------------------------------------------------------------------------------------------
# Profile

frame_profile = Frame(frame_content, highlightthickness=1, highlightbackground="black", width=300, height=250)
frame_profile.grid(row=0, column=0, sticky="W", padx=30)
frame_profile.grid_propagate(0)

profile_img = load_image("Image/male_profile.png", 145, 100)

label_profile = Label(frame_profile, text="Profile", font=('Arial', 20))
label_profile.grid(row=0, column=0, pady=10, sticky="W", padx=10)

# empty label with weight=1 to expand and take up extra space in column 1
empty_label = Label(frame_profile)
empty_label.grid(row=0, column=1, sticky="E", padx=10)
frame_profile.columnconfigure(1, weight=1)

def onclick_edit1():
    os.system("python News_sources_codes/edit1_gui.py")

# edit button for profile
img_edit = load_image("Image/edit.png",30, 30)
button_edit1 = Button(frame_profile, image=img_edit, command=onclick_edit1)
button_edit1.grid(row=0, column=2, sticky="E", padx=10)

label_profile_image = Label(frame_profile, image=profile_img, text="", compound="top", highlightthickness=1, highlightbackground="black")
label_profile_image.grid(row=1, column=0, padx=40, columnspan=3,pady=5)

label_name = Label(frame_profile, text="Alibaba Mohammad Ali Bin",  font=('Arial', 12), fg="#808080")
label_name.grid(row=2, column=0, pady=10, sticky="WE", columnspan=3)



#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------
# About
frame_about = Frame(frame_content, highlightthickness=1, highlightbackground="black", width=300, height=300)
frame_about.grid(row=1, column=0, sticky="W", padx=30)
frame_about.grid_propagate(0)

label_about = Label(frame_about, text="About", font=('Arial', 20))
label_about.grid(row=0, column=0, pady=10, sticky="W", padx=10)

# empty label with weight=1 to expand and take up extra space in column 1
empty_label2 = Label(frame_about)
empty_label2.grid(row=0, column=1, sticky="E", padx=10)
frame_about.columnconfigure(1, weight=1)

def onclick_edit2():
    os.system("python News_sources_codes/edit2_gui.py")

# edit button for profile
button_edit2 = Button(frame_about, image=img_edit, command=onclick_edit2)
button_edit2.grid(row=0, column=2, sticky="E", padx=10)

label_E = Label(frame_about, text="Email", font=('Arial', 12))
label_E.grid(row=1, column=0, padx=40, columnspan=3, sticky="W",pady=3)

label_email = Label(frame_about, text="Alibaba123456@gmail.com", font=('Arial', 10, 'underline'), fg="#808080", compound="bottom")
label_email.grid(row=2, column=0, pady=2, sticky="W", padx=40)

label_P = Label(frame_about, text="Password", font=('Arial', 12))
label_P.grid(row=3, column=0, padx=40, columnspan=3, sticky="W",pady=3)

label_password = Label(frame_about, text="123456", font=('Arial', 10, 'underline'), fg="#808080", compound="bottom")
label_password.grid(row=4, column=0, pady=2, sticky="W", padx=40)

label_G = Label(frame_about, text="Gender", font=('Arial', 12))
label_G.grid(row=5, column=0, padx=40, columnspan=3, sticky="W",pady=3)

label_gender = Label(frame_about, text="Male", font=('Arial', 10, 'underline'), fg="#808080", compound="bottom")
label_gender.grid(row=6, column=0, pady=2, sticky="W", padx=40)

label_A = Label(frame_about, text="Age", font=('Arial', 12))
label_A.grid(row=7, column=0, padx=40, columnspan=3, sticky="W",pady=3)

label_age = Label(frame_about, text="123456", font=('Arial', 10, 'underline'), fg="#808080", compound="bottom")
label_age.grid(row=8, column=0, pady=2, sticky="W", padx=40)
#---------------------------------------------------------------------------------------


#---------------------------------------------------------------------------------------
# History
frame_history = Frame(frame_content, highlightthickness=1, highlightbackground="black", width=1100, height=550)
frame_history.grid(row=0, column=2, padx=30, rowspan=9, columnspan=8)
frame_history.grid_propagate(0)

label_history = Label(frame_history, text="History", font=('Arial', 20))
label_history.grid(row=0, column=0, pady=10, sticky="W", padx=10)

#--------------------------------------------------------------------------------------
# structure




def on_button_click():
    print("Button clicked!")
img_path = "Image/news_row1_1.jpeg"
title = "We're in the AOL phase of artificial intelligence, tech CEO says, as industry raves about A.I."
button_frame = nw3.ButtonFrame(frame_history, img_path, title, '2022-05-05', command=on_button_click)
button_frame2 = nw3.ButtonFrame(frame_history, img_path, "title", '2022-05-05', command=on_button_click)
button_frame.grid(row=1, column=0, pady=3, padx=10)
button_frame2.grid(row=2, column=0, pady=3, padx=10)

button_frame3 = nw3.ButtonFrame(frame_history, img_path, title, '2022-05-05', command=on_button_click)
button_frame4 = nw3.ButtonFrame(frame_history, img_path, title, '2022-05-05', command=on_button_click)
#button_frame5 = nw3.ButtonFrame(frame3, img_path, title, '2022-05-05', command=on_button_click)

button_frame3.grid(row=1, column=1, pady=5, padx=10)
button_frame4.grid(row=2, column=1, pady=5, padx=10)

#--------------------------------------------------------------------------------------



button_load = Button(content_frame, text="Load More", font=font, bg=bg_color, fg=fg_color, padx=15, pady=5, width=13)
button_load.grid(row=3, column=0, columnspan=3, sticky="E", padx=30, pady=15)


root.mainloop()
