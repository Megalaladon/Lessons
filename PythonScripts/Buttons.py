import tkinter
from tkinter import *

root = Tk()

def Myclick():
    MyLabel = Label(root, text='Look! I clicked a button!')
    MyLabel.pack()
#you can use hex codes for colours
myButton =  Button(root,text='Click Me!',padx=50,pady=30, command=Myclick,fg="blue",bg="red")

myButton.pack()

root.mainloop()
