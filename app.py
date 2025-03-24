import tkinter as tk
from tkinter import ttk

root = tk.Tk()

main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True)

tk.Label(main, text="Label top (1)", bg="red").pack(side="top", expand=True, fill="both")
tk.Label(main, text="Label top (2)", bg="orange").pack(side="top", expand=True, fill="both")
tk.Label(root, text="Label left", bg="green").pack(side="left", expand=True, fill="both")


root.mainloop()
