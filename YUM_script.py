from tkinter import *
from tkinter import Tk, Label, Button, StringVar, Toplevel, mainloop
from tkinter import E, N, S, W
import os, subprocess, time


top = Toplevel()
top.title('YUM Installation')
top.geometry('200x140')
init = Label(top, text="Starting application install").grid(row=0, columnspan=2, pady=10, padx=10)
#time.sleep(2)
first_label = subprocess.Popen(['sudo', 'yum','update'],shell=False, input="")
#output = Button(top, text='run', command=first_label)
top.close_button = Button(top, text="Back", command=top.destroy, bg='grey', font='black')
top.close_button.grid(pady=5,padx=10)

if first_label:
    WAI = Label(top, text="Application installed sucessfully")
    WAI.grid(row=5, columnspan=1,padx=10, pady=10)
#def script():
#    top =Toplevel()


top=Toplevel
mainloop()