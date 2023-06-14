import os
import numpy as np
import random
import tkinter as tk
from tkinter import ttk

data_path = "D:\Anime"

def button_clicked():
    folder_names = [name for name in os.listdir(data_path) if os.path.isdir(os.path.join(data_path, name))]
    max_number = (len(folder_names)-1)
    random_number = random.randint(0, max_number)
    
    output_label.config(text= folder_names[random_number])

window = tk.Tk()
window.title("Click the fckin button")

button = tk.Button(window, text="Click Me", command=button_clicked, padx =20)
button.pack()

arial = ("Arial", 20, "bold italic")
arial1 = ("Arial", 15)

text = tk.Label(window, text="VVhat you should vvatch next :", pady=10, font=arial1)
text.pack()
output_label = tk.Label(window, text="Output Text", pady=50, font=arial)
output_label.pack()
window_width = 400
window_height = 200

window.geometry(f"{window_width}x{window_height}")

# Start the Tkinter event loop
window.mainloop()