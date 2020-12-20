from tkinter import *
from tkinter import Tk, Label, Button, StringVar, Toplevel, mainloop
from tkinter import E, N, S, W
import os, subprocess, time


top = Toplevel()
top.title('Pacman Installation')
#top.geometry('300x300')
update2 = subprocess.Popen(['sudo', 'pacman', '-Syu'], stdout=subprocess.PIPE, shell=False)
print (update2.stdout, time.sleep(3))
#close button
top.close_button = Button(top, text="Back", command=top.destroy, bg='grey', font='black')
top.close_button.grid(pady=10,padx=50)
time.sleep(4)
application = ['Pip','Brave_browser']
#init = Label(top, text="Getting " + application[0]).grid(row=1, columnspan=2, pady=10, padx=50)
pip = ['sudo', 'pacman', '-S', 'python-pip']
time.sleep(4)
first_label = subprocess.Popen((pip),shell=False,stdout=subprocess.PIPE)
print(first_label.returncode)
#init2 = Label(top, text="Getting " + application[1]).grid(row=2, columnspan=2, pady=10, padx=50)

Brave_browser = ['sudo', 'pacman', '-S', 'brave-browser']
time.sleep(4)
second_label = subprocess.Popen((Brave_browser),shell=False,stdout=subprocess.PIPE)
print(second_label.returncode)


if first_label:
    print(first_label.returncode)
    WAI = Label(top, text= application[0] + " installed sucessfully")
    WAI.grid(row=1, columnspan=1,padx=50, pady=10)

if second_label:
    print(second_label.returncode)
    WAI = Label(top, text=application[1] + " installed sucessfully")
    WAI.grid(row=2, columnspan=1,padx=50, pady=10)


#def script():


#    top =Toplevel()


top=Toplevel
mainloop()