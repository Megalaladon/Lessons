from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("Sliders")
root.iconbitmap('donkey.ico')
root.geometry("400x400")

def slide(var):
    my_label.config(text=horizontal.get())

def set_value_func():
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

vertical = Scale(root, from_=0, to=400, orient=VERTICAL, command=slide, width=20, length=200)
vertical.pack(fill=Y, side=LEFT)

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL, command=slide, length=400)
horizontal.pack(fill=X)

my_btn = Button(root, text="Set Value", command=set_value_func)
my_btn.pack()

my_label = Label(root, text=horizontal.get())
my_label.pack()

root.mainloop()

