from tkinter import *
#root gui window
root=Tk()
root.title("Loan Calculator")
root.geometry("440x350")
root.configure(bg="cyan")

#compute function to compute both simple and compund interest and display it in the widget
def compute(l,r,t):
 try:
    l=float(l)
    r=float(r)/1200
    t=float(t)
    mp=l*r/(1-1/(1+r)**(t*12))
    tp=mp*12*t
    r=5.454545
    a="{:.2f}".format(mp)
    b="{:.2f}".format(tp)
    r1.set(a)
    r2.set(b)
 except:
    r1.set("")
    r2.set("")

#clear function for removing all the input values in all the Entry boxes
def clear():
    loan.delete(0,"end")
    year.delete(0,"end")
    rate.delete(0,"end")
    r1.set("")
    r2.set("")

#Enter rate
l=Label(root,text="Annual Interest Rate:    ",font=("Times New Roman", 18),bg="cyan")
l.place(relx = 0.3,rely = 0.1,anchor = 'center')
rate=Entry(root,width=25,justify = RIGHT)
rate.place(relx = 0.7,rely = 0.1,anchor = 'center')

#Enter year
l=Label(root,text="Number of Years: ",font=("Times New Roman", 18),bg="cyan")
l.place(relx = 0.3,rely = 0.2,anchor = 'center')
year=Entry(root,width=25,justify = RIGHT)
year.place(relx = 0.7,rely = 0.2,anchor = 'center')

#Enter loan
l=Label(root,text="Loan Amount: ",font=("Times New Roman", 18),bg="cyan")
l.place(relx = 0.3,rely = 0.3,anchor = 'center')
loan=Entry(root,width=25,justify = RIGHT)
loan.place(relx = 0.7,rely = 0.3,anchor = 'center')

#ouptuts
monthlyPayment=Label(root,text="Monthly Payment: ",font=("Times New Roman", 18),bg="cyan")
monthlyPayment.place(relx = 0.3,rely = 0.4,anchor = 'center')

totalPayment=Label(root,text="Total Payment: ",font=("Times New Roman", 18),bg="cyan")
totalPayment.place(relx = 0.3,rely = 0.5,anchor = 'center')

#submit button
button = Button(root,text="Compute Payment",font=("Times New Roman", 12),fg="red",bg="yellow",width=16,height=1,command=lambda:compute(loan.get(),rate.get(),year.get()))
button.place(relx = 0.7,rely = 0.7,anchor = 'center')

#clear button
clr=Button(root,text="Clear",font=("Times New Roman", 12),fg="red",bg="yellow",width=16,height=1,command=lambda:clear())
clr.place(relx=0.3,rely=0.7,anchor='center')

#Monthly Payment

r1=StringVar()
monthlyPayment=Label(root,textvariable=r1,bg="cyan")
monthlyPayment.place(relx = 0.88,rely = 0.4,anchor = 'e')
#Total Payment
r2=StringVar()
totalPayment=Label(root,textvariable=r2,bg="cyan")
totalPayment.place(relx = 0.88,rely = 0.5,anchor = 'e')


root.mainloop()
