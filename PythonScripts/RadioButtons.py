from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Select your pizza")
root.iconbitmap('donkey.ico')

#r = IntVar()
#r.set(2)

MODES = [("Pepperoni","Pepperoni"),("Cheese","Cheese"),("Vegetarian","Vegetarian"),("Mushroom","Mushroom")]

pizza = StringVar()
pizza.set('Pepperoni')

for text,mode in MODES:
    Radiobutton(root,text=text,variable=pizza,value=mode).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text="Pizza with " + value)
    myLabel.pack()

    

#Radiobutton(root,text="Option 1",variable=r,value=1,command=lambda:clicked(r.get())).grid(row=0,column=0)

#Radiobutton(root,text="Option 2",variable=r,value=2,command=lambda: clicked(r.get())).grid(row=1,column=0)

#myLabel = Label(root,text=pizza.get())
#myLabel.pack()

myButton = Button(root,text="Click Me!",command = lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()
