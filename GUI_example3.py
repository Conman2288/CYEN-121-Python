from tkinter import *

window = Tk()
label1 = Label(window, text="A", bg="red", fg="white")
label1.pack(fill=X)

lablel2 = Label(window, text="B", bg="green", fg="white")
label2.pack(fill=BOTH, expand=1)

lablel3 = Label(window, text="C", bg="blue", fg="white")
label3.pack(fill=X)

window.mainloop()
