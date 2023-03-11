from tkinter import *

window = Tk()

label1 = Label(window, text="A label")
label1.grid(row=0, column=0, sticky=W)

label2 = Label(window, text="Another label")
label2.grid(row=1, column=0, sticky=W)

entry1=Entry(window)
entry1.grid(row=0, column=1)

entry2=Entry(window)
entry2.grid(row=1,column=1)

window.mainloop()
