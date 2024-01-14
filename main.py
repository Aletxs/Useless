import time
import tkinter
from tkinter import *
from tkinter import ttk

window = Tk()

window.title("Big Brain")
window.geometry("300x120")
window.iconbitmap('Icon.ico')

Label(window, text="Enter a number").pack()
num = Entry(window, width=35)
num.pack()

rep = num.get()


def calcul():
    popup = Toplevel(window)

    text = tkinter.StringVar()
    text.set("connection with your brain...")

    Label(popup, textvariable=text).pack()

    progressBar = ttk.Progressbar(popup, orient=HORIZONTAL, length=300, mode='determinate', value=0)
    progressBar.pack()

    for i in range(100):
        progressBar["value"] = i + 1
        window.update()
        time.sleep(0.1)

    text.set("Your number is : " + num.get())


Button(window, text="Guess", command=calcul).pack()

window.mainloop()
