from tkinter import *
from tkinter import Tk, Label, Button, StringVar, Toplevel, mainloop
from tkinter import E, N, S, W
import os, subprocess

def apt_install():
    global apt_install
    top = Toplevel()
    top.title('APT-GET Installation')
    top.geometry('250x130')
    start = Label(top, text="Starting application install").grid(row=0, columnspan=2, pady=10, padx=10)
    args = ['sudo', 'apt-get', 'update']
    args2 = ['sudo', 'apt-get', 'upgrade -y']
#subprocess start    
    updating = subprocess.Popen(args,stdout=subprocess.PIPE,shell=False)
    upgrading = subprocess.Popen(args2,stdin=updating.stdout,stdout=subprocess.PIPE, shell=False)
    updating.stdout.close()
#exit button    
    top.close_button = Button(top, text="Back", command=top.destroy, bg='grey', font='black')
    top.close_button.grid(pady=5,padx=10)

    if updating and updating:
        wai = Label(top, text="system updated")
        wai.grid(row=5, columnspan=1,padx=10, pady=10)
    elif start:
        wai2 = Label(top, text="system upgraded")
        wai2.grid(row=5, columnspan=1,padx=10, pady=10)
def script():
    top =Toplevel()


top=Toplevel
mainloop()