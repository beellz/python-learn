import tkinter as tk


window = tk.Tk()

window.title("my first tkinter")
window.minsize(width=500, height=300)

mylabel = tk.Label(text="I am Beellz", font=("Arial", 24, "bold"))

mylabel.pack()

window.mainloop()
