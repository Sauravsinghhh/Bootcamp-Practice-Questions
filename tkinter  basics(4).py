import tkinter as tk

def refresh_window():
    window.update()
    window.update_idletasks()
    print("Refresh completed.")

window = tk.Tk()
window.geometry("300x300")
window.title("Basics of Tkinter")

label = tk.Label(window, text="Click the below button to refresh the window.")
label.pack()

button = tk.Button(window, text="Refresh", command=refresh_window)
button.pack()

window.mainloop()