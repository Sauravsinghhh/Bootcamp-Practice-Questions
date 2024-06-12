import tkinter as tk
from tkinter import messagebox

def on_submit():
    info = (
        f"Name: {name_entry.get()}\n"
        f"Age: {age_entry.get()}\n"
        f"Gender: {gender_var.get()}\n"
        f"Email: {email_entry.get()}\n"
        f"Phone: {phone_entry.get()}"
    )
    messagebox.showinfo("Submission Status", "Information submitted successfully!")
    print(info)

root = tk.Tk()
root.title("Person Info Form")
root.configure(bg='black')

fields = ["Name", "Age", "Email", "Phone"]
entries = {}

for i, field in enumerate(fields):
    tk.Label(root, text=f"{field}:", bg='black', fg='white').grid(row=i, column=0, padx=10, pady=5, sticky="e")
    entries[field] = tk.Entry(root)
    entries[field].grid(row=i, column=1, padx=10, pady=5)

tk.Label(root, text="Gender:", bg='black', fg='white').grid(row=len(fields), column=0, padx=10, pady=5, sticky="e")
gender_var = tk.StringVar()
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male", bg='black', fg='white', selectcolor='black').grid(row=len(fields), column=1, padx=10, pady=5, sticky="w")
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female", bg='black', fg='white', selectcolor='black').grid(row=len(fields)+1, column=1, padx=10, pady=5, sticky="w")

submit_button = tk.Button(root, text="Submit", command=on_submit, bg='white')
submit_button.grid(row=len(fields)+2, column=0, columnspan=2, pady=10)

name_entry = entries["Name"]
age_entry = entries["Age"]
email_entry = entries["Email"]
phone_entry = entries["Phone"]

root.mainloop()
