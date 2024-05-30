from tkinter import *
import webbrowser


myframe = Tk()
myframe.title("Open Link App 🔗")
myframe.geometry("500x300")

mylabel = Label(myframe,text="OPEN LINK 🔗",font="Tahoma 20 bold",pady=30)
mylabel.pack()

mytext = Entry(myframe,width=40)
mytext.pack(pady=30,padx=10)

def open_link():
    inputValue = mytext.get()
    webbrowser.open(f"{inputValue}")
    
myButton = Button(myframe,text="Go",fg="blue",bg="yellow",activebackground="blue",activeforeground="yellow",font="Tahoma 10 bold", padx=20,pady=5,command=open_link)
myButton.pack()


myframe.mainloop()

