import tkinter as tk
from tkinter import ttk

def greet() -> None:
    """print a greeting"""
    print("Hello world!")


root = tk.Tk()

greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack()

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack()

root.mainloop()
