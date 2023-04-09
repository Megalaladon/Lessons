from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("FileDialogs")
root.iconbitmap('donkey.ico')


def open():
    global my_image
    root.filename = filedialog.askopenfilename(
        initialdir="C:/",
        title="Select A File",
        filetypes=(("jpeg files", "*.jpeg"),("Jpg files","*.jpg"),("All Files","*.*"))
    )
    my_label=Label(root,text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_imgage_label = Label(image=my_image).pack()


my_btn = Button(root,text="Open File",command =open).pack()
root.mainloop()
