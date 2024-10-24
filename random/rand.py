import os
import numpy as np
import random
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

data_path = None  #your path

def select_file():
    # Open file dialog and store the selected file path
    global data_path
    data_path = filedialog.askdirectory()
    if data_path:
        label.config(text=f'Selected: {data_path}')
    else:
        label.config(text="No file selected.")


def button_clicked():
    global data_path
    folder_names = [name for name in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, name))]
    max_number = (len(folder_names)-1)
    random_number = random.randint(0, max_number)
    
    output_label.config(text= folder_names[random_number])

window = tk.Tk()
window.title("Title Randomizer")

# Create a button to trigger the file dialog
button1 = tk.Button(window, text="Select File", command=select_file)
button1.pack(pady=20)

# Label to display the selected file path
label = tk.Label(window, text="No file selected.")
label.pack(pady=10)

button2 = tk.Button(window, text="Randomize", command=button_clicked, padx =20)
button2.pack()

arial = ("Arial", 20, "bold italic")
arial1 = ("Arial", 15)

text = tk.Label(window, text="What you should vvatch next :", pady=10, font=arial1)
text.pack()
output_label = tk.Label(window, text="Output Text", pady=50, font=arial)
output_label.pack()
window_width = 400
window_height = 400

window.geometry(f"{window_width}x{window_height}")

# Start the Tkinter event loop
window.mainloop()
