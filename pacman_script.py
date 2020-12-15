from tkinter import *
from tkinter import Tk, Label, Button, StringVar, Toplevel, mainloop
from tkinter import E, N, S, W
import os, subprocess, time


top = Toplevel()
top.title('Pacman Installation')
top.geometry('200x140')
init = Label(top, text="Starting application install").grid(row=0, columnspan=2, pady=10, padx=10)
pip = ['sudo', 'pacman', '-S', 'python-pip']
#user = Entry(top,)
first_label = subprocess.Popen((pip),shell=False,stdout=subprocess.PIPE,text=True)
first_label.wait(4)
#time.sleep(4)
print(first_label.stdout)
#close button
top.close_button = Button(top, text="Back", command=top.destroy, bg='grey', font='black')
top.close_button.grid(pady=5,padx=10)

if first_label == 0:
    WAI = Label(top, text="Application installed sucessfully")
    WAI.grid(row=5, columnspan=1,padx=10, pady=10)
#def script():
#    top =Toplevel()


top=Toplevel
mainloop()