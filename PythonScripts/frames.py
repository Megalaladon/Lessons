from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("ImageViewer")
root.iconbitmap('donkey.ico')

my_img1 = ImageTk.PhotoImage(Image.open("wollongong.jpeg"))
my_img2 = ImageTk.PhotoImage(Image.open('tree.jpg'))

image_list = [my_img1, my_img2]
current_image = 0

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

status_bar = Label(root, text=f"Image {current_image+1} of {len(image_list)}", bd=1, relief=SUNKEN, anchor=E)
status_bar.grid(row=2, column=0, columnspan=3, sticky=W+E)

def forward():
    global current_image
    global my_label
    global button_forward
    global button_back 
    
    current_image += 1
    if current_image == len(image_list) - 1:
        button_forward = Button(root, text='>>', state=DISABLED)
    else:
        button_forward = Button(root, text='>>', command=forward)
        
    my_label.grid_forget()
    my_label = Label(image=image_list[current_image])
    button_back = Button(root, text="<<", command=back)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    
    status_bar.config(text=f"Image {current_image+1} of {len(image_list)}")

def back():
    global current_image
    global my_label
    global button_forward
    global button_back 
    
    current_image -= 1
    if current_image == 0:
        button_back = Button(root, text='<<', state=DISABLED)
    else:
        button_back = Button(root, text='<<', command=back)
        
    my_label.grid_forget()
    my_label = Label(image=image_list[current_image])
    button_forward = Button(root, text=">>", command=forward)
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)
    
    status_bar.config(text=f"Image {current_image+1} of {len(image_list)}")

button_back = Button(root, text="<<", state=DISABLED)
button_exit = Button(root, text="Exit Program", command=root.quit)
button_forward = Button(root, text=">>", command=forward)

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()
