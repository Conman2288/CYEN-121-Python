
#############################################
# Name: Connor Heard
# Date: 2 / 1 / 2023
# Description: Rpi Activity 3 - The Reckoner
#############################################
from tkinter import *

# global variable checks to see if there is currently a result being displayed
equal_pressed = False

# the main GUI
class MainGUI(Frame):
    # the constructor
    def __init__(self, parent):
        Frame.__init__(self, parent, bg="white")
        #parent.attributes("-fullscreen", True)
        self.setupGUI()

    # sets up the GUI
    def setupGUI(self):
        # the calculator uses the TexGyreAdventor font
        # the display
        # right-align text in the display; and set its background to
        # white, its height ot 2 characters, and its font to 50
        # point TexGyreAdventor
        self.display = Label(self, text="", anchor=E, bg="white", height=1, width=15, font=("TexGyreAdventor", 45))
        # put it in the top row, spanning across four columns and
        # expand it on all four sides
        self.display.grid(row=0, column=0, columnspan=4, sticky=E+W+N+S)

        # configure the rows and columns of the Frame to adjust to the window
        # there are 6 rows (0 through 5)
        for row in range(6):
            Grid.rowconfigure(self, row, weight=1)
        # there are 4 columns (0 through 3)
        for column in range(4):
            Grid.columnconfigure(self, column, weight=1)

        # the first row
        # first, fetch and store the image
        img = PhotoImage(file="images/lpr.gif")

        # next, create a button (white background, no border, no highlighting, no color when clicked)
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("("))

        # set the button's image
        button.image = img

        # put the button in its proper row and column
        button.grid(row=1, column=0, sticky=N+S+E+W)

        # the same is done for the rest of the buttons

        img = PhotoImage(file="images/rpr.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process(")"))
        button.image = img
        button.grid(row=1, column=1, sticky=N+S+E+W)

        img = PhotoImage(file="images/clr.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("AC"))
        button.image = img
        button.grid(row=1, column=2, sticky=N+S+E+W)

        img = PhotoImage(file="images/bak.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("back"))
        button.image = img
        button.grid(row=1, column=3, sticky=N+S+E+W)

        # the second row
        # 7
        img = PhotoImage(file="images/7.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("7"))
        button.image = img
        button.grid(row=2, column=0, sticky=N+S+E+W)

        # 8
        img = PhotoImage(file="images/8.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("8"))
        button.image = img
        button.grid(row=2, column=1, sticky=N+S+E+W)

        # 9
        img = PhotoImage(file="images/9.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("9"))
        button.image = img
        button.grid(row=2, column=2, sticky=N+S+E+W)

        # division
        img = PhotoImage(file="images/div.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("/"))
        button.image = img
        button.grid(row=2, column=3, sticky=N+S+E+W)
        
        # the third row
        # 4
        img = PhotoImage(file="images/4.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("4"))
        button.image = img
        button.grid(row=3, column=0, sticky=N+S+E+W)
        
        # 5
        img = PhotoImage(file="images/5.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("5"))
        button.image = img
        button.grid(row=3, column=1, sticky=N+S+E+W)

        # 6
        img = PhotoImage(file="images/6.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("6"))
        button.image = img
        button.grid(row=3, column=2, sticky=N+S+E+W)

        # *
        img = PhotoImage(file="images/mul.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("*"))
        button.image = img
        button.grid(row=3, column=3, sticky=N+S+E+W)

        # the fourth row
        # 1
        img = PhotoImage(file="images/1.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("1"))
        button.image = img
        button.grid(row=4, column=0, sticky=N+S+E+W)

        # 2
        img = PhotoImage(file="images/2.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("2"))
        button.image = img
        button.grid(row=4, column=1, sticky=N+S+E+W)

        # 3
        img = PhotoImage(file="images/3.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("3"))
        button.image = img
        button.grid(row=4, column=2, sticky=N+S+E+W)

        # -
        img = PhotoImage(file="images/sub.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("-"))
        button.image = img
        button.grid(row=4, column=3, sticky=N+S+E+W)

        # the fifth row
        # 0
        img = PhotoImage(file="images/0.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("0"))
        button.image = img
        button.grid(row=5, column=0, sticky=N+S+E+W)

        # .
        img = PhotoImage(file="images/dot.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("."))
        button.image = img
        button.grid(row=5, column=1, sticky=N+S+E+W)

        # +
        img = PhotoImage(file="images/add.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("+"))
        button.image = img
        button.grid(row=5, column=3, sticky=N+S+E+W)

        # the sixth row
        # =
        img = PhotoImage(file="images/eql-wide.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("="))
        button.image = img
        button.grid(row=6, column=0, columnspan=2, sticky=N+S+E+W)

        # **
        img = PhotoImage(file="images/pow.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("**"))
        button.image = img
        button.grid(row=6, column=2, sticky=N+S+E+W)

        # %
        img = PhotoImage(file="images/mod.gif")
        button = Button(self, bg="white", image=img, borderwidth=0, highlightthickness=0, activebackground="white", command=lambda: self.process("%"))
        button.image = img
        button.grid(row=6, column=3, sticky=N+S+E+W)
        
        # pack the GUI
        self.pack(fill=BOTH, expand=1)


    # this function is invoked to check if a result is present and erases it when a new button is pressed    
    def check_if_result_present(self):
        global equal_pressed
        if (equal_pressed):
            self.display["text"] = ""
            equal_pressed = False
    
    # processes button presses    
    def process(self, button):
        
        global equal_pressed
        
        # If the display reads ERROR, then the screen will clear when a new button is pressed
        if (self.display["text"] == "ERROR"):
            self.display["text"] = ""

        self.check_if_result_present()
            
        # AC clears the display
        if (button == "AC"):
            
            # clear the display
            self.display["text"] = ""
            
        # = starts an evaluation of whatever is on the display
        elif (button == "="):
            
            # get the expression in the display
            expr = self.display["text"]
            
            # the evaluation may return an error!
            try:                
                # evaluate the expression
                result = eval(expr)
                
                # store the result to the display
                self.display["text"] = str(result)
                equal_pressed = True
                
            # handle if an error occurs during evaluation
            except:
                # note the error in the display
                self.display["text"] = "ERROR"

        # if button equals back, then the previous input is erased
        elif (button == "back"):
            str_holder = self.display["text"]
            self.display["text"] = str_holder[:-1]
            
        # otherwise, just tack on the appropriate operand
        else:
            self.display["text"] += button

        # checks to see if current input is greater than 14
        if (len(self.display["text"]) > 14):
            str_holder = self.display["text"]
            self.display["text"] = str_holder[:11] + "..."


##############################
# the main part of the program
##############################

# create the window
window = Tk()

#set the window title
window.title("The Reckoner")

# generate the GUI
p = MainGUI(window)

# display the GUI and wait for user interaction
window.mainloop()
