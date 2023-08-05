To Make Easy Tkinter Entry Validations

Example :

from tkinter import *

from EasyTkValidations.Validations import EntryValidation

root = Tk()

root.geometry('500x450')

e1 = Entry(root)

e1.place(x=0, y=0)

EntryValidation(entry_widget=e1, entry_placeholder='Enter Value', s=1)

s = 1 : Accept String Values is True.

root.mainloop()