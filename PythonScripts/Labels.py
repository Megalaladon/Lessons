
from tkinter import *

root = Tk()

#Creating A Label Widget
MyLabel1 = Label(root, text = 'Hello World!')
MyLabel2 = Label(root, text = 'My Name Is Megh Gupta')

#Shoving it onto the screen
MyLabel1.grid(row = 0, column=0)
MyLabel2.grid(row = 1, column=0)

root.mainloop()
