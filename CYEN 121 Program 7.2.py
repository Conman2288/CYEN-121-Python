###########################################
# Name: Connor Heard
# Date: 2 / 8 / 2023
# Description: Program 7 - Input Analyzer
###########################################

from tkinter import *
from spellchecker import SpellChecker

spell = SpellChecker()

# Two global variables that allow for the destruction of the entry field and button of the main window
entry = None
button = None

# A function that takes an arguement and checks to see if its a float data type
def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False

# A function that receives an argument and determines whether that
# argument is a prime number.
def is_prime(x):
    i = 2
    while (i < x):
        if (x % i == 0):
            return False
        i += 1
    return True

# function which analyzes the text put into the entry and returns it to the second window (checks if the input is an integer, float, or string)
def analyze(text):
    global entry
    global button

    # destroy the previous button and entry form of home page
    entry.destroy()
    button.destroy()
    
    analyzed_text = ""

    # checks to see if input is a number and if true, checks to see if the number is a decimal/int, odd/even, prime/composite
    if (text.isnumeric()):
        analyzed_text += "NUMBER (" + str(text) + ")\n"

        if(text.isdigit()):
            analyzed_text += "Integer.\n"
            
            if (int(text) % 2 != 0):
                analyzed_text += "Odd\n"
            else:
                analyzed_text += "Even\n"

            if (is_prime(int(text))):
                analyzed_text += "Prime"

    # checks to see if input is a float data type and returns relevant information
    elif (isfloat(text)):
        analyzed_text += "NUMBER (" + str(text) + ")\n"
        analyzed_text += "Decimal."

    # else the program assumes the input is a string and returns the relevant information
    else:
        analyzed_text += "STRING (" + str(text) + ")\n"
        analyzed_text += str(len(text)) + " characters\n"

    
        # checks to see is input is an actual word and adds it to the label if true        
        if (len(spell.unknown(text.split())) == 0):
            analyzed_text += "Valid English Word"
        # else returns a list of potential closely spelled English words
        else:
            analyzed_text += "Close english words include:\n"
            list_of_similar_words = list(spell.candidates(text))
            count = 0
            for word in list_of_similar_words:
                analyzed_text += str(word) + " "
                count += 1
                if (count % 5 == 0):
                    analyzed_text += "\n"
        
    second_window(analyzed_text)

# This function creates the neccessary widgets related to the main window
def main_window():
    global entry
    global button
    # An entry which gets user input for a word
    entry = Entry(parent)
    entry.grid(row=0, column=0, sticky=E, pady=30)

    # A button which when clicked is supposed to analyze the entry
    button = Button(text="Analyze",command=lambda: [analyze(entry.get())])
    button.grid(row=0, column=1, sticky=W, pady=30, padx=20)

# This function takes in the analyzed words from the main_window's label and prints out the results of the analysis
def second_window(analyzed_word):
    # A label which shows relevant information
    label2 = Label(bg="light grey", fg="black", text=analyzed_word, justify=LEFT)
    label2.grid(row=0, column=0, sticky=E, pady=30)

    #A button which kills the child window and opens up a new parent window
    exit_button = Button(text="Another one", command=lambda: [label2.destroy(),exit_button.destroy(), main_window()])
    exit_button.grid(row=0, column=1, sticky=W, pady=30, padx=20)


################ Main Program ####################
    
# creates a window
parent = Tk()

# creates a title
parent.title("Analyzer ver 1.0")
parent.geometry("400x300")

parent.columnconfigure(0, weight=2)
parent.columnconfigure(1, weight=1)

main_window()

# displays the GUI and waits for user interaction
parent.mainloop()
