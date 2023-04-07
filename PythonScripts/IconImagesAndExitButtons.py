import tkinter
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("IconsandImages")
root.iconbitmap('c:/users/meghg/desktop/donkey.ico')

my_img = ImageTk.PhotoImage(Image.open("wollongong.jpeg"))
mylabel = Label(image=my_img)
mylabel.grid(row=0, column=0)

button_quit = Button(root, text='exit program', command=root.quit)
button_quit.grid(row=1, column=0)

root.mainloop()
