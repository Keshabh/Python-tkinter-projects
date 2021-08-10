from tkinter import *
#root gui window
root=Tk()
root.title("Simple and Compound Interest Calculator")
root.geometry("440x390")

#compute function to compute both simple and compund interest and display it in the widget
def compute(p,r,t):
 try:
    p=float(p)
    r=float(r)
    t=float(t)
    si=(p*r*t)/100
    ci= (p*((1+r/100)**t))-p
    SI.delete(0,"end")
    SI.insert(0,si)
    CI.delete(0,"end")
    CI.insert(0,ci)
 except:
    SI.delete(0,"end")
    SI.insert(0,0)
    CI.delete(0,"end")
    CI.insert(0,0)




#Enter principle
l=Label(root,text="Enter Principle: ",font=("Times New Roman", 18))
l.place(relx = 0.3,rely = 0.1,anchor = 'center')
principle=Entry(root,width=25)
principle.place(relx = 0.7,rely = 0.1,anchor = 'center')

#Enter Rate
l=Label(root,text="Enter Rate: ",font=("Times New Roman", 18))
l.place(relx = 0.3,rely = 0.2,anchor = 'center')
rate=Entry(root,width=25)
rate.place(relx = 0.7,rely = 0.2,anchor = 'center')

#Enter years
l=Label(root,text="Enter Years: ",font=("Times New Roman", 18))
l.place(relx = 0.3,rely = 0.3,anchor = 'center')
years=Entry(root,width=25)
years.place(relx = 0.7,rely = 0.3,anchor = 'center')

#submit button
button = Button(root,text="CALCULATE INTEREST",font=("Times New Roman", 12),fg="white",bg="gray64",width=20,height=1,command=lambda:compute(principle.get(),rate.get(),years.get()))
button.place(relx = 0.5,rely = 0.5,anchor = 'center')

#Compound INTEREST
l=Label(root,text="Compound Interest: ",font=("Times New Roman", 18))
l.place(relx = 0.3,rely = 0.7,anchor = 'center')
CI=Entry(root,width=25)
CI.place(relx = 0.7,rely = 0.7,anchor = 'center')

#simple interest
l=Label(root,text="Simple Interest: ",font=("Times New Roman", 18))
l.place(relx = 0.3,rely = 0.8,anchor = 'center')
SI=Entry(root,width=25)
SI.place(relx = 0.7,rely = 0.8,anchor = 'center')

root.mainloop()
