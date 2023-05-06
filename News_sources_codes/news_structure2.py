from tkinter import *
from PIL import Image, ImageTk

def load_image(file_path):
    img = Image.open(file_path)
    new_img = img.resize((375, 150))
    photo_img = ImageTk.PhotoImage(new_img)
    return photo_img

class news2:
    def __init__(self, root, img1, img2, img3, tittle1, tittle2, tittle3):
        self.root = root
        self.img1 = img1
        self.img2 = img2
        self.img3 = img3
        self.tittle1 = tittle1
        self.tittle2 = tittle2
        self.tittle3 = tittle3

        # Keep a reference to the PhotoImage objects
        self.c1 = None
        self.c2 = None
        self.c3 = None

    def create(self):
        
       

        # Convert image to PhotoImage
        self.c1 = load_image(self.img1)

        # Row 2 elements
        button_row2_1 = Button(self.root, text=self.tittle1, font=('Arial', 10), image=self.c1, compound="top", wraplength=300, anchor="n", justify="center")

    

        # Convert image to PhotoImage
        self.c2 = load_image(self.img2)

        # Row 2 elements
        button_row2_2 = Button(self.root, text=self.tittle2, font=('Arial', 10), image=self.c2, compound="top", wraplength=300, anchor="n", justify="center")

      

        # Convert image to PhotoImage
        self.c3 = load_image(self.img3)

        # Row 2 elements
        button_row2_3 = Button(self.root, text=self.tittle3, font=('Arial', 10), image=self.c3, compound="top", wraplength=300, anchor="n", justify="center")
        button_row2_1.grid(row=0, column=0, pady=10, padx=12)
        button_row2_2.grid(row=0, column=1, pady=10, padx=10)
        button_row2_3.grid(row=0, column=2, pady=10, padx=10)

        button_row2_1.config(height=200)
        button_row2_2.config(height=200)
        button_row2_3.config(height=200)
