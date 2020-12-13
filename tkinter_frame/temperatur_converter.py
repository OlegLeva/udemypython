from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(fahrenheit.get())
        fahren = (value - 32) * 5/9
        celsius.set(float('%.3f' % fahren))
    except ValueError:
        pass

root = Tk()
root.title("fahrenheit to celsius")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S), padx=5, pady=5)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

fahrenheit = StringVar()
fahrenheit_entry = ttk.Entry(mainframe, width=7, textvariable=fahrenheit)
fahrenheit_entry.grid(column=0, columnspan=2, row=1, sticky=(W, E), padx=5, pady=5)

celsius = StringVar(value='Temperatur in celsius')
ttk.Label(mainframe, textvariable=celsius).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=1, columnspan=3, row=3, sticky=(W, E))

ttk.Label(mainframe, text="fahrenheit").grid(column=3, row=1, sticky=W, padx=5, pady=5)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E, padx=5, pady=5)
ttk.Label(mainframe, text="celsius").grid(column=3, row=2, sticky=W, padx=5, pady=5)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

fahrenheit_entry.focus()
root.bind("<Return>", calculate)


root.mainloop()