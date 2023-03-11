from tkinter import *

window = Tk()
a11 = Label(window, text="Hello", bg="cyan", fg="black")
a11.pack(side=LEFT, expand=1, fill=Y)
a12 = Label(window, text="131", bg="magenta", fg="white")
a12.pack(side=LEFT, expand=1, fill=X)
a13 = Label(window, text="Class", bg="orange", fg="white")
a13.pack(side=LEFT, expand=0, fill=BOTH)
window.title("Test1")
window.geometry("400x300")
window.mainloop()
