from tkinter import *
import random
import string

def generate():
    pass1 = string.ascii_letters + string.digits + string.punctuation
    password =""
    for x in range(pwdLen.get()):
        password = password + random.choice(pass1)
        pwd.set(password)


root = Tk()
root.geometry("600x450")
root.resizable(width=False,height=False)
pwd = StringVar()
pwdLen = IntVar()
root.config(background="#C4DFDF")
label =Label(root,text="Password Generator",font="courier 20 bold",pady=10,background="#E3F4F4").pack()
userName = Label(root,text="UserName",font="lucida 16",background="#E3F4F4").place(x=40,y=60)
pass_len = Label(root,text="password length",font="lucida 16",background="#E3F4F4").place(x=40,y=100)
password = Label(root,text="password",font="lucida 16",background="#E3F4F4").place(x=40,y=140)

my_name = Entry(root,width=40,font="lucida 16").place(x=220,y=60)
passLen = Entry(root,width =40,textvariable=pwdLen,font="lucida 16").place(x=220,y=100)
gen_pass =Entry(root,width =40,textvariable=pwd,font="lucida 16").place(x=220,y=140)
btn =Button(root,text="Generate Password",command=generate,width=45,font="courier 15 bold",activebackground = '#93BFCF',background='#6096B4',pady=10).place(x=20,y=200) 
root.mainloop()