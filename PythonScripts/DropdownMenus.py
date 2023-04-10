from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog


def show():
    myLabel = Label(root,text= clicked.get()).pack()

options = ['Monday','Tuesday','Wendsday','Thursday','Friday']

root = Tk()
root.title("DropDownMenus!")
root.iconbitmap("donkey.ico")

clicked = StringVar()
clicked.set(options[0])

myButton = Button(root,text="Show Selection",command=show).pack()
drop =OptionMenu(root,clicked,*options)
drop.pack()


root.mainloop()

