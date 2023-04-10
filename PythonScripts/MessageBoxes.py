from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Message Boxes")
root.iconbitmap('donkey.ico')

def popup():
    response = messagebox.askokcancel("This is my popup","Hello World!")
    Label(root,text=response).pack()
   # if response=="yes":
        #Label(root,text="you clicked yes!").pack()
    #else:
        #Label(root,text="You Clicked NO!").pack()
        

Button(root,text="popup",command=popup).pack()
             
                
root.mainloop()
