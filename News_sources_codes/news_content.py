from tkinter.ttk import Separator
import user_manager
from tkinter import *
from PIL import Image, ImageTk
import news_structure1 as nw1
import news_date as ndate
import news_structure2 as nw2
import os

def load_image(file_path, x, y):
    img = Image.open(file_path)
    new_img = img.resize((x, y))
    photo_img = ImageTk.PhotoImage(new_img)
    return photo_img

root = Tk()

root.title('Main Page')

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

# Create a frame with a black background
frame1 = Frame(root, bg="#1C1C1C", width=1600, height=100)
frame1.pack(fill=X)

# Open image
img = Image.open("Image/news_icon.png")

# Resize image
new_img = img.resize((80, 65))

# Convert image to PhotoImage
photo_img = ImageTk.PhotoImage(new_img)

'''
empty_space = Label(frame1,  bg="#1C1C1C")
empty_space.grid(row=0, column=0, padx=50)
'''

empty_space2 = Label(frame1,  bg="#1C1C1C", width=80)
empty_space2.grid(row=0, column=0)

# Create a label and display the image on the frame
label = Label(frame1, image=photo_img, bg="#1C1C1C")
label.grid(row=0, column=2, padx=30, pady=20)


label_name = Label(frame1, text="NewsNet", font = ("Arial", 20), bg="#1C1C1C", fg="white")
label_name.grid(row=0, column=3, padx=7)

frame2 = Frame(root, bg="#1C1C1C", width=1600, height=10)
frame2.pack(fill=X)




separator = Separator(frame2, orient='horizontal', style='Separator.TSeparator')
separator.pack(fill='x')

empty_space = Label(frame2,  bg="#1C1C1C")
empty_space.pack()

# Create a canvas with scrollbars
canvas = Canvas(root)
scrollbar = Scrollbar(root, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)
canvas.config(yscrollcommand=scrollbar.set)
canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Create a frame to hold the content
content_frame = Frame(canvas, borderwidth=2, relief="groove")

# Bind mouse wheel to scrollbar
def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    if canvas.bbox("all")[1] < 0:
        canvas.yview_scroll(-1, "units")

canvas.bind_all("<MouseWheel>", _on_mousewheel)

# Set the content_frame to expand to fill the window
content_frame.pack(expand=True, fill=BOTH) 

# Set the canvas to expand to fill the content_frame
canvas.create_window((0, 0), window=content_frame, anchor="nw")


#-------------------------------------------------------------------------------------------------------




#-------------------------------------------------------------------------------------------------------
# News

frame_button = Frame(content_frame)
frame_button.grid(row=0, column=0)

def onlick_home(window):
    window.destroy()
    os.system("python News_sources_codes/home_gui.py")

img_home = load_image("Image/home.png",70, 65)
button_home = Button(frame_button, image=img_home, bd=0, highlightthickness=0, command=lambda:onlick_home(root))
button_home.grid(row=0, column=0, padx=65, pady=10)

empty_space1 = Label(frame_button)
empty_space1.grid(row=0, column=1, padx=530)

def onclick_summary():
    os.system("python News_sources_codes/summary_gui.py")

img_summary = load_image("Image/summary.png",70, 65)
button_summary = Button(frame_button, image=img_summary, bd=0, highlightthickness=0, command=onclick_summary)
button_summary.grid(row=0, column=2, padx=65, pady=10)


frame_news = Frame(content_frame, width=100, borderwidth=2, relief="groove")
frame_news.grid(row=1, column=0, padx=100)



# set anchor to center and wraplength to 300 pixels
tittle = Label(frame_news, text="We're in the AOL phase of artificial intelligence, tech CEO says, as industry raves about A.I.", width=80, anchor="center", wraplength=900, font=('Arial', 20, 'bold'))

tittle.grid(row=0, column=0)

label_date = Label(frame_news, text="🕛 23 January 2023", fg="grey" ,font=('Arial', 12))
label_date.grid(row=1, column=0)


label_aurthor = Label(frame_news, text="| By Alibaba Hii Bin Mohammad", fg="grey" ,font=('Arial', 12))
label_aurthor.grid(row=2, column=0)

empty_space3 = Label(frame_news)
empty_space3.grid(row=3, column=0)

img_news = load_image("Image/news_row1_1.jpeg", 500, 300)
label_img_news = Label(frame_news, image=img_news)
label_img_news.grid(row=4, column=0, pady=10)

empty_space4 = Label(frame_news)
empty_space4.grid(row=5, column=0)


frame_text = Frame(frame_news, width=100)
frame_text.grid(row=6, column=0, pady=20)

# Add text to the Text widget
long_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed auctor vitae nisl ut consectetur. Pellentesque nec orci velit. Nam lobortis lorem ut massa tincidunt, sit amet aliquet orci eleifend. Proin bibendum lectus non lorem consequat, non eleifend ante tristique. Aliquam ut faucibus quam, nec interdum nulla. Sed tempor leo quis elit vestibulum aliquet. Vestibulum maximus, enim eu venenatis ultricies, sapien ex pharetra sapien, vel dictum velit nulla ac mi. Nulla eget ipsum id urna sagittis blandit. Donec ac purus tincidunt, molestie metus nec, accumsan mauris. Maecenas tincidunt fringilla mauris, quis rutrum tellus fermentum eget. Praesent et enim ut eros eleifend ultrices in nec dolor. Donec eu tortor vitae nulla bibendum consequat eget sed nisl. Suspendisse suscipit massa lectus, eget faucibus ante vestibulum in. Vestibulum et velit ac elit faucibus maximus a a massa. Sed blandit erat dui, id ultrices odio mollis eget. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed auctor vitae nisl ut consectetur. Pellentesque nec orci velit. Nam lobortis lorem ut massa tincidunt, sit amet aliquet orci eleifend. Proin bibendum lectus non lorem consequat, non eleifend ante tristique. Aliquam ut faucibus quam, nec interdum nulla. Sed tempor leo quis elit vestibulum aliquet. Vestibulum maximus, enim eu venenatis ultricies, sapien ex pharetra sapien, vel dictum velit nulla ac mi. Nulla eget ipsum id urna sagittis blandit. Donec ac purus tincidunt, molestie metus nec, accumsan mauris. Maecenas tincidunt fringilla mauris, quis rutrum tellus fermentum eget. Praesent et enim ut eros eleifend ultrices in nec dolor. Donec eu tortor vitae nulla bibendum consequat eget sed nisl. Suspendisse suscipit massa lectus, eget faucibus ante vestibulum in. Vestibulum et velit ac elit faucibus maximus a a massa. Sed blandit erat dui, id ultrices odio mollis eget."

# Set anchor to center and wraplength to 900 pixels
text_label = Label(frame_text, text=long_text, font=('Arial', 12), wraplength=900, justify="left")
text_label.pack()

empty_space5 = Label(frame_news)
empty_space5.grid(row=7, column=0, pady=40)
#-------------------------------------------------------------------------------------------------------
# Update the canvas scroll region
canvas.create_window((0, 0), window=content_frame, anchor=NW)
content_frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

root.mainloop()