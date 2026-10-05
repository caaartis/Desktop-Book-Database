"""
A program that stores this book information:
Title,Author, Year,ISBN

User can:
View all records

Search an entry
Add an entry
Update an entry
Delete entry
close a program

"""

from tkinter import *
import backend

def update_command():
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get())


def view_command():
    list1.delete(0,END)
    for row in backend.view():
        list1.insert(END,row)
def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END,row)
def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0,END)
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()))
def get_selected_row(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[4])
    return(selected_tuple)
def delete_command():
    backend.delete(selected_tuple[0])

window=Tk()
window.wm_title("BookStore")
# window.geometry("800x600")
# frame=Frame(window,width=800,height=800)
# frame.pack()
#
# window.title("Python Database app")



#Create four labels

l1=Label(window,text="Title")
l1.grid(row=0,column=0)
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)
l2=Label(window,text="Author")
l2.grid(row=0,column=2)
author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

l3=Label(window,text="Year")
l3.grid(row=1,column=0)
year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

l4=Label(window,text="ISBN")
l4.grid(row=1,column=2)
isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

#Add buttons

button_1=Button(window,text="View All",height=1,width=10,command=view_command)
button_1.grid(row=2,column=3)
button_2=Button(window,text="Search entry",height=1,width=10,command=search_command)
button_2.grid(row=3,column=3)
button_3=Button(window,text="Add entry",height=1,width=10,command=add_command)
button_3.grid(row=4,column=3)
button_4=Button(window,text="Update",height=1,width=10,command=update_command)
button_4.grid(row=5,column=3)
button_5=Button(window,text="Delete",height=1,width=10,command=delete_command)
button_5.grid(row=6,column=3)
button_6=Button(window,text="Close",height=1,width=10,command=window.destroy)
button_6.grid(row=7,column=3)
list1=Listbox(window,height=22,width=35)
list1.grid(row=2,column=0)
scroll1=Scrollbar(window)
scroll1.grid(row=2,column=2,rowspan=6)
list1.configure(yscrollcommand=scroll1.set)
scroll1.configure(command=list1.yview)
list1.bind('<<ListboxSelect>>',get_selected_row)
window.mainloop()
