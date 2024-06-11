import tkinter as tk
from tkinter import messagebox

def on_button_click():
    messagebox.showinfo("Message", "Saurav is Good Human!")

root = tk.Tk()
root.title("Tkinter Example")
root.geometry("300x200")

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=20)

root.mainloop()
