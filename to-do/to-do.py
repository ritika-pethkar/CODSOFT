from tkinter import *
from tkinter import messagebox

def newTask():
  task = my_entry.get()
  if task!="":
    lb.insert(END,task)
    my_entry.delete(0,"end")
  else:
    messagebox.showwarning("Warning","Please enter a Task first")

def del_task():
  lb.delete(ANCHOR)
# creating main Window
todo_root = Tk()
todo_root.geometry('500x450')
todo_root.title("To-Do List")
todo_root.config(bg= '#DBDFEA')
todo_root.resizable(width= False , height= False)

# Creating widgets
frame = Frame(todo_root)
frame.pack(pady= 15)

lb = Listbox(
    frame,
    width= 30,
    height= 8,
    font = ('Times',18),
    bd =0,
    fg ='Black',
    highlightthickness=0,
    selectbackground= '#ACB1D6',
    activestyle='none',
)
lb.pack(side = LEFT,fill = BOTH)

tasks = []
for item in tasks:
  lb.insert(END,item)

sb = Scrollbar(frame,background="grey")
sb.pack(side=RIGHT,fill= BOTH)
lb.config(yscrollcommand=sb.set)
sb.config(command= lb.yview)

my_entry = Entry(
  todo_root,
  font=('times',20)
)
my_entry.pack(pady = 20)

btn_frame = Frame(todo_root)
btn_frame.pack(pady =20)
addTask_btn = Button(
    btn_frame,
    text = 'Add Task',
    font =('times',15),
    background= '#8294C4',
    padx = 20,
    pady = 10,
    command= newTask
)
addTask_btn.pack(fill = BOTH , expand = True, side = LEFT)
delTask_btn = Button(
  btn_frame,
  text= "Remove Task",
  font =('times',15),
  bg = '#8294C4',
  padx = 20,
  pady =10,
  command= del_task
)
delTask_btn.pack(fill = BOTH,expand= True,side =LEFT)


todo_root.mainloop()