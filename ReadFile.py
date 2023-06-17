import tkinter as tk
from tkinter import filedialog
import sqlite3

def readPic():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()

    print("Selected file path:", file_path)

    # Read the image file in binary mode
    with open(file_path, "rb") as image_file:
        binary_data = image_file.read()

    image = binary_data
    print(image)
