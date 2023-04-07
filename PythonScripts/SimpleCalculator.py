import tkinter
from tkinter import *



root = Tk()
root.title("Simple Calculator")

e = Entry(root,width = 35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
#e.insert(INSERT,"Put your desired number in here")

def button_click(number):
    #e.delete(0,END)
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)
    
def button_add():
    first_number = e.get()
    global f_num 
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0,END)
    
def button_equal():
    second_number = e.get()
    e.delete(0,END)
    
    if math=="addition":
        e.insert(0,f_num+int(second_number))
    if math =="subtraction":
        e.insert(0,f_num-int(second_number))
    if math =="multiplication":
        e.insert(0,f_num*int(second_number))
    if math == "division":
        e.insert(0,f_num/int(second_number))

def button_subtract():
    first_number = e.get()
    global f_num 
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0,END)

def button_multiply():
    first_number = e.get()
    global f_num 
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0,END)

def button_divide():
    first_number = e.get()
    global f_num 
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0,END)

#Defines Buttons
Button_1 = Button(root,text="1",padx=40,pady=20,command= lambda: button_click(1))
Button_2 = Button(root,text="2",padx=40,pady=20,command= lambda: button_click(2))
Button_3 = Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3))
Button_4 = Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))
Button_5 = Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5))
Button_6 = Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6))
Button_7 = Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
Button_8 = Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8))
Button_9 = Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9))
Button_0 = Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0))
Button_Add = Button(root,text="+",padx=39,pady=20,command= button_add)
Button_Equal=Button(root,text="=",padx=91,pady=20,command=button_equal)
Button_Clear = Button(root,text="Clear",padx=79,pady=20,command=lambda: button_clear())
Button_Subtract = Button(root,text="-",padx=41,pady=20,command= button_subtract)
Button_Multiply= Button(root,text="*",padx=40,pady=20,command= button_multiply)
Button_Divide= Button(root,text="/",padx=41,pady=20,command= button_divide)

#Put the buttons the screen
Button_1.grid(row=3,column=0)
Button_2.grid(row=3,column=1)
Button_3.grid(row=3,column=2)

Button_4.grid(row=2,column=0)
Button_5.grid(row=2,column=1)
Button_6.grid(row=2,column=2)

Button_7.grid(row=1,column=0)
Button_8.grid(row=1,column=1)
Button_9.grid(row=1,column=2)

Button_0.grid(row=4,column=0)
Button_Clear.grid(row=4,column=1,columnspan=2)
Button_Add.grid(row=5,column=0)
Button_Equal.grid(row=5,column=1,columnspan=2)
Button_Subtract.grid(row=6,column=0)
Button_Multiply.grid(row=6,column=1)
Button_Divide.grid(row=6,column=2)


root.mainloop()
