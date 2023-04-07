import tkinter
from tkinter import *



root = Tk()


e = Entry(root,width = 50, bg="blue",fg="white",borderwidth=5)
e.pack()
e.insert(0,"Enter your name,credit card details and age")


def Myclick():
    MyLabel = Label(root, text=e.get())
    MyLabel.pack()
#you can use hex codes for colours
myButton =  Button(root,text='Enter your full name, age credit card details and a survey for 1000 robux',padx=50,pady=30, command=Myclick,fg="blue",bg="red")

myButton.pack()

root.mainloop()
