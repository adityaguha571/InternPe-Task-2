from tkinter import *
from tkinter.ttk import *
from time import strftime
#tkinter window
root = Tk()
root.title('Digital Clock')
def time():
	string = strftime('%H:%M:%S %p')
	lb.config(text=string)
	lb.after(1000, time)
lb = Label(root, font=('calibri', 40, 'bold','italic'),
			background='black',
			foreground='white')
lb.pack(anchor='center')
time()
mainloop()