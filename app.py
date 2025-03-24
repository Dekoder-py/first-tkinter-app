import tkinter as tk
from tkinter import ttk

def greet() -> None:
    """print a greeting"""
    print("Hello world!")


root = tk.Tk()

# change theme to make it work like it should (i.e. how it works on windows)
s = ttk.Style()
s.theme_use("clam")

greet_button = ttk.Button(root, text="Greet", command=greet)
greet_button.pack(side="top", fill="both", expand=True)

quit_button = ttk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="top", fill="both", expand=True)

root.mainloop()
