from tkinter import *
import tkinter.font as font
'''create a root window'''
root= Tk()
root.title("Simple Calculator")
root.geometry("370x300")
root.configure(bg="grey")

#function to clear the display panel
def clear():
    result.delete(0,"end")


#function calc to display the calculated result
def calc():
  try:
    s=result.get()
    clear()
    result.insert(0,round(eval(s),5))
  except:
     clear()
     result.insert(0,'error!')

#function to change the text of box
def display(val):
    s=result.get()
    clear()
    result.insert(0,s+val)


#add entry box to display the output
result = Entry(root,width=50)
result.grid(row=0,
               column=0,
               padx=10,
               pady=10,
               ipady=10,
               columnspan=30)

buttonFont = font.Font(family='Helvetica', size=10, weight='bold')
#add Calculator buttons
bt1 = Button(root,text="1",fg="black",bg="red",width=10,height=2,font=buttonFont,command=lambda:display("1"))
bt1.grid(column=0,row=2)

bt2 = Button(root,text="2",fg="black",bg="red",width=10,height=2,font=buttonFont,command=lambda:display("2"))
bt2.grid(column=1,row=2)

bt3 = Button(root,text="3",fg="black",bg="red",width=10,height=2,font=buttonFont,command=lambda:display("3"))
bt3.grid(column=2,row=2)

plus = Button(root,text="+",fg="black",bg="red",width=10,height=2,font=buttonFont,command=lambda:display(" + "))
plus.grid(column=3,row=2)

bt4 = Button(root,text="4",fg="black",bg="red",width=10,height=2,font=buttonFont,command=lambda:display("4"))
bt4.grid(column=0,row=3)

bt5 = Button(root,text="5",fg="black",bg="red",width=10,height=2,font=buttonFont,command=lambda:display("5"))
bt5.grid(column=1,row=3)

bt6 = Button(root,text="6",fg="black",bg="red",width=10,height=2,font=buttonFont,command=lambda:display("6"))
bt6.grid(column=2,row=3)

minus = Button(root,text="-",fg="black",bg="red",width=10,height=2,font=buttonFont,command=lambda:display(" - "))
minus.grid(column=3,row=3)

bt7 = Button(root,text="7",fg="black",bg="red",width=10,height=2,font=buttonFont,command=lambda:display("7"))
bt7.grid(column=0,row=4)

bt8 = Button(root,text="8",fg="black",bg="red",width=10,height=2,font=buttonFont,command=lambda:display("8"))
bt8.grid(column=1,row=4)

bt9 = Button(root,text="9",fg="black",bg="red",width=10,height=2,font=buttonFont,command=lambda:display("9"))
bt9.grid(column=2,row=4)

mult = Button(root,text="X",fg="black",bg="red",width=10,height=2,font=buttonFont,command=lambda:display(" * "))
mult.grid(column=3,row=4)

bt0 = Button(root,text="0",fg="black",bg="red",width=10,height=2,font=buttonFont,command=lambda:display("0"))
bt0.grid(column=0,row=5)

clr = Button(root,text="Clear",fg="black",bg="red",width=10,height=2,font=buttonFont,command=lambda:clear())
clr.grid(column=1,row=5)

eql = Button(root,text="=",fg="black",bg="red",width=10,height=2,font=buttonFont,command=lambda:calc())
eql.grid(column=2,row=5)

div = Button(root,text="/",fg="black",bg="red",width=10,height=2,font=buttonFont,command=lambda:display(" / "))
div.grid(column=3,row=5)

dcml = Button(root,text=".",fg="black",bg="red",width=10,height=2,font=buttonFont,command=lambda:display("."))
dcml.grid(row=6,column=0)

'''button = Button(root,text="Click me",fg="blue",command=lambda:display("10"))
#set the position of button using grid method
button.grid(column=0, row=1)'''
root.mainloop()
