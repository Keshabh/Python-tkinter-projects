from tkinter import *
#root gui window
root=Tk()
root.title("Rank Based Percentile Calculator")
root.geometry("440x390")
root.configure(bg='SeaGreen1')


#function to clear all the inputs
def clear():
    rank.delete(0,"end")
    participants.delete(0,"end")
    out.delete(0,"end")

#compute function to compute both simple and compund interest and display it in the widget
def compute(rank,participants):
 try:
    r=int(rank)
    tp=int(participants)
    percentile=((tp-r)/tp)*100
    a="{:.2f}".format(percentile)
    val="Percentile : "+str(a)
    out.delete(0,"end")
    out.insert(0,val)
 except:
    clear()

#Enter total participants
l=Label(root,text="Total Participants: ",font=("Times New Roman", 18),width=15,borderwidth=2,bg='lawn green', relief="solid")
l.place(relx = 0.3,rely = 0.2,anchor = 'center')
participants=Entry(root,width=15,justify='center',font=("Calibri",16))
participants.place(height=33,relx = 0.75,rely = 0.2,anchor = 'center')

#Enter rank
l=Label(root,text="Rank: ",font=("Times New Roman", 18),width=15,borderwidth=2,bg='lawn green', relief="solid")
l.place(relx = 0.3,rely = 0.3,anchor = 'center')
rank=Entry(root,width=15,justify='center',font=("Calibri",16))
rank.place(height=33,relx = 0.75,rely = 0.3,anchor = 'center')

#submit button
button = Button(root,text="Calculate Percentile",font=("Times New Roman", 12),fg="black",bg="firebrick1",width=18,borderwidth=1, relief="solid",height=1,command=lambda:compute(rank.get(),participants.get()))
button.place(relx = 0.5,rely = 0.45,anchor = 'center')

#ouptut
out=Entry(root,width=30,justify='center',font=("Calibri",16))
out.place(height=45,relx = 0.5,rely = 0.6,anchor = 'center')

#clear button
clr = Button(root,text="Clear",font=("Times New Roman", 12),fg="black",bg="firebrick1",borderwidth=1, relief="solid",width=10,height=1,command=lambda:clear())
clr.place(relx = 0.5,rely = 0.75,anchor = 'center')


root.mainloop()
