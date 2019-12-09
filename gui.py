from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048*value*10000.0+0.5)/10000.0)
    except ValueError:
        pass

root = Tk()
root.title("SOPO Sign In") #this is where the name on top of the window goes

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row = 0, sticky =(N, W, E, S))
root.columnconfigure(0, weight = 1)
root.rowconfigure(0, weight=1)




feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=2, sticky=(W, E))

#ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Sign In", command=calculate).grid(column=2, row=5, sticky=W)

ttk.Label(mainframe, text="Please sign in below whenever you visit SOPO").grid(column=1, row=1, sticky=W, columnspan=3)
ttk.Label(mainframe, text="Name: ").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="What is your main reason for coming today?").grid(column=1, row=3, sticky=W, columnspan=3)
phone = StringVar()
home = ttk.Radiobutton(mainframe, text='Repairing my bike', variable=phone, value='use').grid(column=1, row=4)
office = ttk.Radiobutton(mainframe, text='Dropping off donation', variable=phone, value='donate').grid(column=2, row=4)
cell = ttk.Radiobutton(mainframe, text='Volunteering', variable=phone, value='volunteer').grid(column=3, row=4)
#ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)


for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()