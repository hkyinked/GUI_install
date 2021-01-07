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
        wai.grid(row=2, columnspan=1,padx=10, pady=10)
    elif start:
        wai2 = Label(top, text="system upgraded")
        wai2.grid(row=2, columnspan=1,padx=10, pady=10)
def vscode():
    top = Toplevel()
    start = Label(top, text="Starting application install").grid(row=0, columnspan=2, pady=10, padx=10)
    #args2 = ['sudo', 'apt-get', 'install', 'code']
    args = ['sudo', 'apt-get', 'upgrade', '-y']
#subprocess start    
 #   updating = subprocess.Popen(args,stdout=subprocess.PIPE,shell=False)
 #   upgrading = subprocess.Popen(stdin=updating.stdout,stdout=subprocess.PIPE, shell=False)
 #   if updating == True and upgrading == True:
 #      # print(upgrading.stderr)
 #       updating.stdout.close()        
def script():
    top =Toplevel()
    bash = Label(top, text="changing bash").grid(row=3, columnspan=2, pady=10, padx=10)
    with open('~/bash_cpy', 'w+', encoding="utf-8") as f:
        f.readlines()
        for lines in f.readlines:
            if (lines in f.readlines == ('export PS1') or ('PS1=')):
                #file = 'This works'
                #file = """('export PS1="\[$(tput bold)\]\[\033[38;5;128m\]\u\[$(tput sgr0)\] \[$(tput sgr0)\]\[\033[38;5;11m\]>>\[$(tput sgr0)\] \[$(tput sgr0)\]\[$(tput bold)\]\[\033[38;5;166m\]\w\[$(tput sgr0)\]\n\[$(tput sgr0)\]\[$(tput bold)\]\[\033[38;5;1m\]\\$\[$(tput sgr0)\]"')"""
                file = """('export PS1="\[$(tput bold)\]\[\\033[38;5;128m\]\u\[$(tput sgr0)\] \[$(tput sgr0)\]\[\\033[38;5;11m\]>>\[$(tput sgr0)\] \[$(tput sgr0)\]\[$(tput bold)\]\[\\033[38;5;166m\]\w\[$(tput sgr0)\]\n\[$(tput sgr0)\]\[$(tput bold)\]\[\033[38;5;1m\]\\$\[$(tput sgr0)\]"')"""
                f.write(file)
                f.close()
            print(f)
        cats = subprocess.run('cat', '~/bashrc_cpy')
        print(cats)


top=Toplevel
mainloop()
