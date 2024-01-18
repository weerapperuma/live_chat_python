import tkinter as tk
from tkinter import ttk

def on_button_click():
    label.config(text="Hello, " + entry.get())

# Create the main window
root = tk.Tk()
root.title("SERVER")

# Create and add widgets (labels, buttons, entry fields, etc.)
label = ttk.Label(root, text="Enter your name:")
label.grid(column=0, row=0, padx=100, pady=100)

entry = ttk.Entry(root)
entry.grid(column=1, row=0, padx=10, pady=10)

button = ttk.Button(root, text="Say Hello", command=on_button_click)
button.grid(column=2, row=0, padx=100, pady=100)

# Start the main event loop
root.mainloop()
