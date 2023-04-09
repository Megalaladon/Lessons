from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("CheckBoxes")
root.iconbitmap('donkey.ico')

def show():
    myLabel = Label(root,text=var.get()).pack()


var = StringVar()

c=Checkbutton(root,text="Would you like to supersize your order, check this box!",variable=var,onvalue="Supersize",offvalue="Regular Size")
c.deselect()
c.pack()


myButton = Button(root,text="Show Selection",command=show).pack()

root.mainloop()

