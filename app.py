import tkinter as tk
from tkinter import ttk

def greet() -> None:
    """print a greeting"""
    print(f"Hello {user_name.get().title() or "World"}!")  # prints Hello and the user's name or hello world when no name is provided


root = tk.Tk()

user_name = tk.StringVar()

input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame.pack(fill="both")

name_label = ttk.Label(input_frame, text="Name: ")
name_label.pack(side="left")
name_entry = ttk.Entry(input_frame, width=15, textvariable=user_name)
name_entry.pack(side="left")
name_entry.focus()


buttons = ttk.Frame(root, padding=(20, 10))
buttons.pack(fill="both")

greet_button = ttk.Button(buttons, text="Greet", command=greet)
greet_button.pack(side="left")

quit_button = ttk.Button(buttons, text="Quit", command=root.destroy)
quit_button.pack(side="left")

root.mainloop()
