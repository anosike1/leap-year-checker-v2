# this is second version of our LEAP YEAR CHECKER program
# unlike the first version, leaving the box EMPTY and clicking the CHECK button
# tells you if our CURRENT year is a leap year.

# import tkinter
from tkinter import *
from datetime import *

# define the window title
window = Tk()
window.title ("LEAP YEAR CHECKER")

# define the label
label1 = Label (text="Insert Year Here:")
label1.grid (column=0,row=1)
# this will be an empty label where it'll give the report
label2 = Label ()
label2.grid (column=1, row=4)

# define the entry where the user will insert the year to be checked
entry = Entry ()
entry.grid (column=1, row=1)

# create a function called CHECK which does the following:
def check(): 
    # if the user inputs a data, it assigns this data to the variable x  
    if bool (entry.get())==True:
        x = int(entry.get())
    # if the user inputs nothing, it takes the user's CURRENT year and assigns it to x
    else:        
        x = date.today().year
    # then everything continues as in the previous version
    
    # if the year is not evenly divisible by 4, it is NOT a leap year
    if x%4==0:
        # if the year is divisble by 4 and NOT divisible by 100, it IS a leap year
        if x%100==0:
    # if the year is divisible by 4,100, and 400, it IS a leap year
            if x%400==0:
                y = "Leap Year!"
            else:
                y = "Not a Leap Year!"
        else:
            y = "Leap Year!"
    else:
        y = "Not a Leap Year!"
# The report will be stored in the 'y' variable
# anc the empty label will be configured with the text

    label2.config (text=f"{x} is {y}")

# create a button named CHECK which will call the check function when clicked
buttn = Button (text="CHECK",command=check)
buttn.grid (row=2, column=1)

# activate the program
mainloop()