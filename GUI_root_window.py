'''create a Gui root window having menu bar, with text, button, input, which concatenates
 user input and changes the initial text with new text'''
#import everything from tkinter package for GUI interface
'''create a root window with specific geometry'''
from tkinter import *
#create an object via of Tk() class via which we can access our root window
root=Tk()
#provide a title to the page
root.title("Welcome to GUI World!")
#set the geometry of window (width x height )
root.geometry('450x200')

'''add a menu to your  window '''
#lets add a menu bar in a root window using Menu class
menu = Menu(root)
item = Menu(menu)
#add cascade adds menu labels in the menue
menu.add_cascade(label='File', menu=item)
#add command adds the label inside the menue label
item.add_command(label='New')
item.add_command(label='Open')
item.add_command(label='Info')
item.add_command(label='Save')
item.add_command(label='Save as')
#config saves it
root.config(menu=menu)
menu.add_cascade(label='Home')
menu.add_cascade(label='Insert')
menu.add_cascade(label='Design')
menu.add_cascade(label='Layout')
menu.add_cascade(label='Referneces')
menu.add_cascade(label='Mailings')

'''add some text in ur window, take input from user, and a function that changes text'''
#now lets put a text in the window using Label class
l=Label(root,text="Are you a Geek?")
#lets define the position where we want to keep our text using grid() method, by default its (0,0)
l.grid()
#adding an entry field to take input from user using Entry class
txt=Entry(root,width=10)
#using grid provide it the position next to the text
txt.grid(column=1, row=0)
#we will create a function which will change the text in the window and concatenate user input ,if button is clicked
def clicked():
    #concatenated new text with user input text
    res = "You wrote " + txt.get()  #we used get() method to get text inside txt object
    #we will use configure method of Label class to change the text
    l.configure(text=res)

'''create a button'''
#now we will create the button using Button class
button = Button(root,text="Click me",fg="blue",command=clicked)
#set the position of button using grid method
button.grid(column=2, row=0)

'''execute the window to run it until it close it'''
#lets show the window using mainloop
root.mainloop()
