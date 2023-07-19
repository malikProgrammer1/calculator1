# calculator1
# Calculator created by myself and @dheller307. Completed on July 19th, 2023; during the summer entering our senior year of highschool.

from tkinter import *
from tkinter import ttk

def press(num):
  new = input.get()
  new = new + str(num)
  input.set(new)

def calculate(*args):
    try:
        value = eval(input.get())
        input.set(value)
    except ValueError:
        pass

def back(*args):
  x=input.get()
  input.set(x[0:-1])

def clear(*args):
  x = input.get()
  input.set(x[1:1])
      
root = Tk()
root.title("Calculator")

solution = StringVar()

mainframe = ttk.Frame(root, padding="5 6 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

input = StringVar()
input_entry = ttk.Entry(mainframe, width=6, textvariable=input)
input_entry.grid(columnspan=5, row=1, sticky=(W, E))

ttk.Button(mainframe, text="1", command=lambda: press('1')).grid(column=1, row=2, sticky=W)
ttk.Button(mainframe, text="2", command=lambda: press('2')).grid(column=2, row=2, sticky=W)
ttk.Button(mainframe, text="3", command=lambda: press('3')).grid(column=3, row=2, sticky=W)
ttk.Button(mainframe, text="4", command=lambda: press('4')).grid(column=1, row=3, sticky=W)
ttk.Button(mainframe, text="5", command=lambda: press('5')).grid(column=2, row=3, sticky=W)
ttk.Button(mainframe, text="6", command=lambda: press('6')).grid(column=3, row=3, sticky=W)
ttk.Button(mainframe, text="7", command=lambda: press('7')).grid(column=1, row=4, sticky=W)
ttk.Button(mainframe, text="8", command=lambda: press('8')).grid(column=2, row=4, sticky=W)
ttk.Button(mainframe, text="9", command=lambda: press('9')).grid(column=3, row=4, sticky=W)
ttk.Button(mainframe, text="0", command=lambda: press('0')).grid(column=1, row=5, sticky=W)
ttk.Button(mainframe, text=".", command=lambda: press('.')).grid(column=2, row=5, sticky=W)
ttk.Button(mainframe, text="⌫", command=back).grid(column=1, row=6, sticky=W)
ttk.Button(mainframe, text="clear", command=clear).grid(column=2, row=6, sticky=W)
ttk.Button(mainframe, text="=", command=calculate).grid(column=5, row=6, sticky=N)
ttk.Button(mainframe, text="+", command=lambda: press('+')).grid(column=5, row=2, sticky=W)
ttk.Button(mainframe, text="-", command=lambda: press('-')).grid(column=5, row=3, sticky=W)
ttk.Button(mainframe, text="x", command=lambda: press('*')).grid(column=5, row=4, sticky=W) 
ttk.Button(mainframe, text="÷", command=lambda: press('/')).grid(column=5, row=5, sticky=W)
ttk.Button(mainframe, text="π", command=lambda: press('3.14')).grid(column=4, row=2, sticky=W)
ttk.Button(mainframe, text="e", command=lambda: press('2.718')).grid(column=4, row=3, sticky=W)
ttk.Button(mainframe, text="^", command=lambda: press('**')).grid(column=4, row=4, sticky=W)
ttk.Button(mainframe, text="(-)", command=lambda: press('-')).grid(column=4, row=5, sticky=W)
ttk.Button(mainframe, text="%", command=lambda: press('/100')).grid(column=4, row=6, sticky=W)
ttk.Button(mainframe, text="(", command=lambda: press('(')).grid(column=3, row=5, sticky=W)
ttk.Button(mainframe, text=")", command=lambda: press(')')).grid(column=3, row=6, sticky=W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

input_entry.focus
root.bind("<Return>", calculate)
root.mainloop()
