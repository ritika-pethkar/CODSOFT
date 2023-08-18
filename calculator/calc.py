from tkinter import *
from tkinter import messagebox

cal_root = Tk()
cal_root.geometry("654x750")
cal_root.title('My-Calculator')
cal_root.config(background= '#9384D1')
cal_root.resizable(height=False,width=False)

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text== "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value="Error!"
        scvalue.set(value)
        screen.update    
    
    elif text == "C":
        scvalue.set("")
        screen.update
    
    else:
        scvalue.set(scvalue.get()+text)

scvalue = StringVar()
scvalue.set("")
screen = Entry(
    cal_root,
    textvariable = scvalue,
    font= 'lucida 40 '
)
screen.pack(fill = X,ipadx= 8,pady=10,padx=10)

btn_frame = Frame(cal_root,bg='#C9A7EB')
f1 = Frame(btn_frame,bg='#C9A7EB')
btn = Button(f1,text="9",padx=17,pady=10,font= 'lucida 30',background='#E3DFFD',width=3)
btn.pack(side= LEFT,fill = BOTH,padx=25,pady=12)
btn.bind("<Button-1>",click)
btn = Button(f1,text="8",padx=17,pady=10,font= 'lucida 30',background='#E3DFFD',width=3)
btn.pack(side= LEFT,fill = BOTH,padx=18,pady=12)
btn.bind("<Button-1>",click)
btn = Button(f1,text="7",padx=17,pady=10,font= 'lucida 30',background='#E3DFFD',width=3)
btn.pack(side= LEFT,fill = BOTH,padx=18,pady=12)
btn.bind("<Button-1>",click)
btn = Button(f1,text="6",padx=17,pady=10,font= 'lucida 30',background='#E3DFFD',width=3)
btn.pack(side= LEFT,fill = BOTH,padx=18,pady=12)
btn.bind("<Button-1>",click)
f1.pack()

f2 = Frame(btn_frame,bg='#C9A7EB')
btn = Button(f2,text="5",padx=17,pady=10,font= 'lucida 30',background='#E3DFFD',width=3)
btn.pack(side= LEFT,fill = BOTH,padx=18,pady=12)
btn.bind("<Button-1>",click)
btn = Button(f2,text="4",padx=17,pady=10,font= 'lucida 30',background='#E3DFFD',width=3)
btn.pack(side= LEFT,fill = BOTH,padx=18,pady=12)
btn.bind("<Button-1>",click)
btn = Button(f2,text="3",padx=17,pady=10,font= 'lucida 30',background='#E3DFFD',width=3)
btn.pack(side= LEFT,fill = BOTH,padx=18,pady=12)
btn.bind("<Button-1>",click)
btn = Button(f2,text="2",padx=17,pady=10,font= 'lucida 30',background='#E3DFFD',width=3)
btn.pack(side= LEFT,fill = BOTH,padx=18,pady=12)
btn.bind("<Button-1>",click)
f2.pack()

f3 = Frame(btn_frame,bg='#C9A7EB')
btn = Button(f3,text="1",padx=17,pady=10,font= 'lucida 30',background='#E3DFFD',width=3)
btn.pack(side= LEFT,fill = BOTH,padx=18,pady=12)
btn.bind("<Button-1>",click)
btn = Button(f3,text="0",padx=19,pady=10,font= 'lucida 30',background='#E3DFFD',width=3)
btn.pack(side= LEFT,fill = BOTH,padx=18,pady=12)
btn.bind("<Button-1>",click)
btn = Button(f3,text="+",padx=19,pady=10,font= 'lucida 30',background='#E3DFFD',width=3)
btn.pack(side= LEFT,fill = BOTH,padx=18,pady=12)
btn.bind("<Button-1>",click)
btn = Button(f3,text="-",padx=19,pady=10,font= 'lucida 30',background='#E3DFFD',width=3)
btn.pack(side= LEFT,fill = BOTH,padx=18,pady=12)
btn.bind("<Button-1>",click)
f3.pack()

f4 = Frame(btn_frame,bg='#C9A7EB')

btn = Button(f4,text="/",padx=19,pady=10,font= 'lucida 30',background='#E3DFFD',width=3)
btn.pack(side= LEFT,fill = BOTH,padx=18,pady=12)
btn.bind("<Button-1>",click)
btn = Button(f4,text="*",padx=19,pady=10,font= 'lucida 25',background='#E3DFFD',width=3)
btn.pack(side= LEFT,fill = BOTH,padx=18,pady=12)
btn.bind("<Button-1>",click)
btn = Button(f4,text="%",padx=19,pady=10,font= 'lucida 28',background='#E3DFFD',width=3)
btn.pack(side= LEFT,fill = BOTH,padx=18,pady=12)
btn.bind("<Button-1>",click)
btn = Button(f4,text="C",padx=19,pady=10,font= 'lucida 28',background='#E3DFFD',width=3)
btn.pack(side= LEFT,fill = BOTH,padx=18,pady=12)
btn.bind("<Button-1>",click)
f4.pack()

f5 = Frame(btn_frame,bg='#C9A7EB')
btn = Button(f5,text="=",padx=19,pady=10,font= 'lucida 28',background='#E3DFFD',width=300)
btn.pack(side= LEFT,fill = BOTH,padx=18,pady=12)
btn.bind("<Button-1>",click)


f5.pack()
btn_frame.pack(padx=10,pady=10)
cal_root.mainloop()