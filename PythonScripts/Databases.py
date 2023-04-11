

from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import sqlite3

root = Tk()
root.title("Databases!")
root.iconbitmap("donkey.ico")
 
#Databases

#Create a database or connect to one

conn = sqlite3.connect('adress_book.db')


#Create cursor
c = conn.cursor()

#Create Table

#c.execute("""CREATE TABLE adresses(
        #first_name text,
       # last_name text,
       # adresses text,
       # city text,
       # state text,
       # zipcode integer)""")
       
#Create Sumbit function

def sumbit():
    conn = sqlite3.connect('adress_book.db')
    c = conn.cursor()
    c.execute("INSERT INTO adresses VALUES(:f_name,:l_name,:adress,:city,:state,:zipcode)",
              {
                  'f_name':f_name.get(),
                  'l_name':l_name.get(),
                  'adress':adresses_name.get(),
                  'city':city_name.get(),
                  'state':state_name.get(),
                  'zipcode':zipcode_name.get(),
                  })
    conn.commit()
    conn.close()
    
    #Clear the text boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    adresses_name.delete(0,END)
    city_name.delete(0,END)
    state_name.delete(0,END)
    zipcode_name.delete(0,END)
    
def query():
    conn = sqlite3.connect('adress_book.db')
    c = conn.cursor()
    #Query Database
    
    c.execute("SELECT *,oid FROM adresses")
    records = c.fetchall()
    print(records)
    
    print_records = ""
    #Loop thru results
    
    
    for record in records:
        print_records += str(record) + "\n"
        
    query_label = Label(root,text=print_records)
    query_label.grid(row=8,column=0,columnspan=2)
    
    conn.commit()
    conn.close()
    

    
#Create text boxes
f_name = Entry(root,width=30)
f_name.grid(row=0,column=1,padx=20,)


l_name = Entry(root,width=30)
l_name.grid(row=1,column=1,padx=20,)

adresses_name = Entry(root,width=30)
adresses_name.grid(row=2,column=1,padx=20,)

city_name = Entry(root,width=30)
city_name.grid(row=3,column=1,padx=20,)

state_name = Entry(root,width=30)
state_name.grid(row=4,column=1,padx=20,)

zipcode_name = Entry(root,width=30)
zipcode_name.grid(row=5,column=1,padx=20,)

#crete textbox labels

f_name_label = Label(root,text="First Name")
f_name_label.grid(row=0,column=0)

l_name_label = Label(root,text="Lastname")
l_name_label.grid(row=1,column=0)

adress_name_label = Label(root,text="Adress")
adress_name_label.grid(row=2,column=0)

city_name_label = Label(root,text="City")
city_name_label.grid(row=3,column=0)

state_name_label = Label(root,text="State")
state_name_label.grid(row=4,column=0)

zipcode_name_label = Label(root,text="Zipcode")
zipcode_name_label.grid(row=5,column=0)
#Create submit button

sumbit_button = Button(root,text="Add Record to Database",command=sumbit)
sumbit_button.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#Create a Query button


    

Query_Button = Button(root,text="Show Records",command = query)
Query_Button.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)



#Commit Changes
conn.commit()



#Close Connection

conn.close()

root.mainloop()