from tkinter import *
from PIL import Image, ImageTk

class news1:
    def __init__(self, img1, img2, img3, img4, img5, tittle1, tittle2, tittle3, tittle4, tittle5, root):
        self.img1 = img1
        self.img2 = img2
        self.img3 = img3
        self.img4 = img4
        self.img5 = img5
        self.tittle1 = tittle1
        self.tittle2 = tittle2
        self.tittle3 = tittle3
        self.tittle4 = tittle4
        self.tittle5 = tittle5
        self.root = root
        
        # Keep a reference to the PhotoImage objects
        self.row2_1 = None
        self.row2_2_1 = None
        self.row2_2_2 = None
        self.row2_2_3 = None
        self.row2_2_4 = None
    
    def create(self):
        global row2_1, row2_2_1, row2_2_2, row2_2_3, row2_2_4
        # Open and resize image
        img_row2_1 = Image.open(self.img1)
        new_img_row2_1 = img_row2_1.resize((550, 250))

        # Convert image to PhotoImage
        row2_1 = ImageTk.PhotoImage(new_img_row2_1)

        # Row 2 elements
        button_row2_1 = Button(self.root, text=self.tittle1, image=row2_1, compound="top")

        # Second Frame on row 2
        frame_row2_2 = Frame(self.root)


        # Second Frame on row 2 - subframes
        frame_row2_2_1 = Frame(frame_row2_2)
        frame_row2_2_1.grid(row=0, column=0)

        frame_row2_2_2 = Frame(frame_row2_2)
        frame_row2_2_2.grid(row=0, column=1)

        frame_row2_2_3 = Frame(frame_row2_2)
        frame_row2_2_3.grid(row=1, column=0)

        frame_row2_2_4 = Frame(frame_row2_2)
        frame_row2_2_4.grid(row=1, column=1)


        # Open and resize image
        img_row2_2_1 = Image.open(self.img2)
        new_img_row2_2_1 = img_row2_2_1.resize((300, 108))

        img_row2_2_2 = Image.open(self.img3)
        new_img_row2_2_2 = img_row2_2_2.resize((300, 108))

        img_row2_2_3 = Image.open(self.img4)
        new_img_row2_2_3 = img_row2_2_3.resize((300, 108))

        img_row2_2_4 = Image.open(self.img5)
        new_img_row2_2_4 = img_row2_2_4.resize((300, 108))

      


        # Convert image to PhotoImage
        row2_2_1 = ImageTk.PhotoImage(new_img_row2_2_1)
        row2_2_2 = ImageTk.PhotoImage(new_img_row2_2_2)
        row2_2_3 = ImageTk.PhotoImage(new_img_row2_2_3)
        row2_2_4 = ImageTk.PhotoImage(new_img_row2_2_4)

        # Row 2 frame 2 button 1
        button_row2_2_1 = Button(frame_row2_2, text=self.tittle2, image=row2_2_1, compound="top")
        button_row2_2_1.grid(row=0,column=0, padx=5, pady=5)

        # Row 2 frame 2 button 2
        button_row2_2_2 = Button(frame_row2_2, text=self.tittle3, image=row2_2_2, compound="top")
        button_row2_2_2.grid(row=0, column=1, padx=5, pady=5)

        # Row 2 frame 2 button 3
        button_row2_2_3 = Button(frame_row2_2, text=self.tittle4, image=row2_2_3, compound="top")
        button_row2_2_3.grid(row=1, column=0, padx=5, pady=5)

        # Row 2 frame 2 button 4
        button_row2_2_4 = Button(frame_row2_2, text=self.tittle5, image=row2_2_4, compound="top")
        button_row2_2_4.grid(row=1, column=1, padx=5, pady=5)


        # Row 2
        empty_space1 = Label(self.root)
        empty_space1.grid(row=0, column=0, padx=12)
        button_row2_1.grid(row=0, column=1, pady=10, padx=3)
        frame_row2_2.grid(row=0, column=2)

       