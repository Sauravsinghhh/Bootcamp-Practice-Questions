import tkinter as tk
from tkinter import messagebox

def show_form():
    enroll_button.destroy()
    
    tk.Label(root, text="Name:", bg='black', fg='white').grid(row=1, column=0, padx=10, pady=5, sticky="e")
    name_entry.grid(row=1, column=1, padx=10, pady=5)
    
    tk.Label(root, text="Age:", bg='black', fg='white').grid(row=2, column=0, padx=10, pady=5, sticky="e")
    age_entry.grid(row=2, column=1, padx=10, pady=5)
    
    tk.Label(root, text="Field of Study:", bg='black', fg='white').grid(row=3, column=0, padx=10, pady=5, sticky="e")
    study_entry.grid(row=3, column=1, padx=10, pady=5)
    
    submit_button.grid(row=4, column=0, columnspan=2, pady=10)

def on_submit():
    info = (
        f"Name: {name_entry.get()}\n"
        f"Age: {age_entry.get()}\n"
        f"Field of Study: {study_entry.get()}"
    )
    messagebox.showinfo("Enrollment Status", "You Enrolled in the course successfully!")
    print(info)  

root = tk.Tk()
root.title("Course Enrollment")
root.configure(bg='black')

enroll_button = tk.Button(root, text="I am happy to enroll in the course", command=show_form, bg='white')
enroll_button.grid(row=0, column=0, columnspan=2, pady=10)

name_entry = tk.Entry(root)
age_entry = tk.Entry(root)
study_entry = tk.Entry(root)

#
submit_button = tk.Button(root, text="Submit", command=on_submit, bg='white')

root.mainloop()
