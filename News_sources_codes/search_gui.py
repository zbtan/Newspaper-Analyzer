import user_manager
from tkinter import *
from PIL import Image, ImageTk
import news_structure1 as nw1
import news_date as ndate
import news_structure2 as nw2
import news_structure3 as nw3
import os

root = Tk()
root.title('Main Page')

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))


# Create a canvas with scrollbars
canvas = Canvas(root)
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.config(yscrollcommand=scrollbar.set)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Create a frame to hold the content
content_frame = Frame(canvas)

# Bind mouse wheel to scrollbar
def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", _on_mousewheel)

# Set the content_frame to expand to fill the window
content_frame.pack(expand=True, fill=BOTH)

# Set the canvas to expand to fill the content_frame
canvas.create_window((0, 0), window=content_frame, anchor="nw")

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

search_button = Button(search_frame, image=photo_img2, borderwidth=0, activebackground="#1C1C1C")
search_button.config(state="disabled")
# Define function to perform search


# Open image
img3 = Image.open("Image/profile.png")

# Resize image
new_img3 = img3.resize((80, 65))

# Convert image to PhotoImage
photo_img3 = ImageTk.PhotoImage(new_img3)

def onclick_profile(window):
    window.destroy()
    os.system("python News_sources_codes/setting_gui.py")

# Create a button and display the image on the frame
button3 = Button(frame1, image=photo_img3, bg="#1C1C1C",  command=lambda:onclick_profile(root))

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


# -----------------------------------------------------------------------------------------------


frame2 = Frame(content_frame)
new_img4 = img2.resize((35, 35))

# Convert image to PhotoImage
photo_img4 = ImageTk.PhotoImage(new_img4)

# Create search button and entry widget
search_entry2 = Entry(frame2,font=('Arial', 25), bd=0, width=28, justify=LEFT)
search_entry2.insert(0, "Search")
frame3 = Frame(content_frame)

def get_entry_text(entry_widget):
    text = entry_widget.get()
    print(text)
    

    def on_button_click():
        print("Button clicked!")
    img_path = "Image/news_row1_1.jpeg"
    title = "We're in the AOL phase of artificial intelligence, tech CEO says, as industry raves about A.I."
    button_frame = nw3.ButtonFrame(frame3, img_path, title, '2022-05-05', command=on_button_click)
    button_frame2 = nw3.ButtonFrame(frame3, img_path, "title", '2022-05-05', command=on_button_click)
    button_frame.grid(row=0, column=0, pady=3, padx=10)
    button_frame2.grid(row=1, column=0, pady=3, padx=10)
    
    button_frame3 = nw3.ButtonFrame(frame3, img_path, title, '2022-05-05', command=on_button_click)
    button_frame4 = nw3.ButtonFrame(frame3, img_path, title, '2022-05-05', command=on_button_click)
    #button_frame5 = nw3.ButtonFrame(frame3, img_path, title, '2022-05-05', command=on_button_click)

    button_frame3.grid(row=0, column=1, pady=5, padx=10)
    button_frame4.grid(row=1, column=1, pady=5, padx=10)

    button_more = Button(content_frame, text="More", bg="black", fg="white", bd=3, width=20, font=font,height=2)
    button_more.grid(row=3, column=0, sticky="E", padx=88,pady=50)
    
   



search_button2 = Button(frame2, image=photo_img4, borderwidth=0, activebackground="#1C1C1C", command=lambda: get_entry_text(search_entry2))



search_entry2.pack(side=LEFT, padx=5)
search_button2.pack(side=LEFT,padx=5)

frame1.grid(row=0, column=0)
frame2.grid(row=1, column=0, pady=30)
# Add the frame to the content frame grid
frame3.grid(row=2, column=0)
#---------------------------------------------------------------------------------------

# Disable scrollbar if content is shorter than canvas
content_height = content_frame.winfo_reqheight()
canvas_height = canvas.winfo_height()
if content_height <= canvas_height:
    scrollbar.config(command=None)
    canvas.unbind_all("<MouseWheel>")

# Update the canvas scroll region
canvas.create_window((0, 0), window=content_frame, anchor=NW)
content_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))



root.mainloop()
