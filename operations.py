#import the tkinter module first
from tkinter import *
#the window will contantain all the operations to be performed
window =Tk()
window.title("Operations")
window.geometry("600x250")
window.configure(bg="wheat")

#define the function that will be perfomed on the click of the buttons
def add():
    A = float(Entry_1.get())
    B = float(Entry_2.get())
    S  = A + B
    Answer.set(S)

def subtract ():
    A = float(Entry_1.get())
    B = float(Entry_2.get())
    S = A - B
    Answer.set(S)

def multiply ():
    A = float(Entry_1.get())
    B = float(Entry_2.get())
    S = A * B
    Answer.set(S)

def divide ():
    A = float(Entry_1.get())
    B = float(Entry_2.get())
    S = A / B
    Answer.set(S)

def Clear():
    Entry_1.delete(0,END)
    Entry_2.delete(0,END)
    Entry_3.delete(0,END)

#define the labels
Entry_1 = Label(window, text ="First_entry", bg ="white")
Entry_2 = Label(window, text ="Second_entry", bg ="white")
Entry_3= Label(window, text ="Answer", bg ="white")
Entry_1.grid(row = 0, column = 0, sticky=W)
Entry_2.grid(row = 2, column = 0, sticky=W)
Entry_3.grid(row = 4, column = 0, sticky=W)

#define the entry windows where the user types in their input
Entry_1 = Entry(window)
Entry_2 = Entry(window)

#define the variable to be displayed on the entry widow
Answer = StringVar()
Entry_3=Entry(window, textvariable=Answer)

Entry_1.grid(row =0, column=1)
Entry_2.grid(row =2, column=1)
Entry_3.grid(row =4, column=1)

#define button functions
sum_button = Button(window, text = "Add", bg="green", command = add)
sum_button.grid(row=6, column=1)
sum_button = Button(window, text = "Subtract", bg="green", command = subtract)
sum_button.grid(row=6, column=2)
multiply_button = Button(window, text = "Mulitply", bg="green", command = multiply)
multiply_button.grid(row=6, column=3)
divide_button = Button(window, text = "Divide", bg="green", command = divide)
divide_button.grid(row=6, column=4)
Clear = Button(window , text="Clear", bg = "Red", command = Clear)
Clear.grid(row = 7, column = 1)
window.mainloop()