from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("Windows!")
root.iconbitmap('donkey.ico')

def open():
    global my_img
    top = Toplevel()
    Lbl = Label(top,text="Hello World!").pack()
    my_img = ImageTk.PhotoImage(Image.open("wollongong.jpeg"))
    my_label = Label(top,image=my_img).pack()
    top.title("Windows!")
    top.iconbitmap('donkey.ico')
    btn2 = Button(top,text="close window",command=top.destroy).pack()


btn = Button(root,text="Open Second Window!",command=open).pack()
             
                
root.mainloop()
