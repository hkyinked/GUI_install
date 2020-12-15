from tkinter import Tk, Label, Button, StringVar
from tkinter import E, N, S, W
import subprocess, time
from tkinter import Toplevel
from tkinter.constants import COMMAND


top =Toplevel
root = Tk()
root.iconbitmap()

class Installation:
    LABEL_TEXT = [
        "Which Type of Package Manager are you using?"
            ]
    def __init__(self, master):
        self.master = master
        master.title("Installation Script")

        self.label_index = 0
        self.label_text = StringVar()
        self.label_text.set(self.LABEL_TEXT[self.label_index])
        self.label = Label(master, textvariable=self.label_text)
        self.label.bind("<Button-1>", self.cycle_label_text)
        self.label.grid(pady=10,padx=10)
#****APT button****
        self.APT_button = Button(master, text="APT", command=self.APT, bg='grey', font='white')
        self.APT_button.grid(row=3, column=0, sticky=W,pady=10,padx=10)
#****Pacman button****
        self.arch_button = Button(master, text="Pacman", command=self.arch, bg='blue', font='white')
        self.arch_button.grid(row=3,column=0,sticky=N,pady=10,padx=10)
#****YUM button****
        self.centos_button = Button(master, text="YUM", command=self.centos, bg='purple', font='white')
        self.centos_button.grid(row=3,column=0,sticky=E,pady=10,padx=10)
#****Exit button****
        self.close_button = Button(master, text="Exit", command=master.quit, bg='red', font='white')
        self.close_button.grid(columnspan=2,sticky=W+E+S+N,pady=5,padx=10)

#define: APT function
    def APT(self):
        print("Now installing using apt-get!")
        update1 = subprocess.Popen(['sudo', 'apt-get', 'update'], shell=False)
        update01 = subprocess.Popen(['sudo', 'apt-get', 'upgrade', '-y'], shell=False, stdout=subprocess.PIPE)
        print (update01.stderr)
        while update1 and update01 == 0:
            print ('System Updated, Now getting applications!!')
            print ('system upgraded getting applications!!!')
            import APT_script
            importing = subprocess.Popen(args=['*/./APT_script'],stdout=subprocess.PIPE,shell=False, text=True)
            print(importing.stdout)
            print(importing.stderr)
           # importing.stdout.close()
        else:
            if update1 and update01 == 1:
                print(update1.stderr)
                print(update01.stderr)
                print('I broke here!!')

#define: ARCH function
    def arch(self):
        print("Now installing using pacman!")
        update2 = subprocess.run(['sudo', 'pacman', '-Syu'], stdout=subprocess.PIPE, shell=False, text=True)
        while update2:
            print(update2.stdout)
            time.sleep(2)
            print ('system updated getting applications!!!')
            import pacman_script
            importing = subprocess.Popen(args=['*/./pacman_script'],stdout=subprocess.PIPE,shell=False, text=True)
            new_var = importing.stdout.close()
            new_var
        self.new_method(update2)

    def new_method(self, update2):
            if update2 == 1:  
                print(update2.stderr)
                print('I broke here!!')

#define: CENTOS function
    def centos(self):
        print("Now installing using yum!")
        subprocess.run('this is red hat based')

    def cycle_label_text(self, event):
        self.label_index += 1
        self.label_index %= len(self.LABEL_TEXT) # wrap around
        self.label_text.set(self.LABEL_TEXT[self.label_index])

my_gui = Installation(root)
root.mainloop()