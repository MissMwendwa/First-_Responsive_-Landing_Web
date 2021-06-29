from tkinter import *
window = Tk()
window.title ("First_window_app")
window.geometry ("800x400")
window.configure(bg="wheat")

def Calculate():
    Q = int(Entry_1.get())
    P = int(Entry_2.get())
    C = Q*P
    variable.set(C)

def Clear():
    Entry_1.delete(0,END)
    Entry_2.delete(0,END)
    Entry_3.delete(0,END)

L1 = Label(window, text = "Quantity", bg="blue")
L2= Label(window, text = "Price", bg="blue")
L3= Label(window, text = "Cost", bg="blue")
L1.grid(row=0, column=0,sticky=W)
L2.grid(row=0, column=0,sticky=W)
L3.grid(row=0, column=0,sticky=W)

Entry_1=Entry(window)
Entry_2=Entry(window)

variable =StringVar()
Entry_3=Entry(window, textvariable=variable)

Entry_1.grid(row=0,column=1)
Entry_2.grid(row=1,column=1)
Entry_3.grid(row=2,column=1)

button_1=Button(window, text="calculate", bg="purple", command=Calculate)
button_1.grid(row=3, column=1)
button_2=Button(window, text="Clear", bg="blue", command = Clear)
button_2.grid(row=3, column=2)
window.mainloop()

