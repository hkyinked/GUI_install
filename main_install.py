from os import close
from tkinter import Tk, Label, Button, StringVar
from tkinter import E, N, S, W
import subprocess, time, os
from tkinter import Toplevel
from tkinter.constants import COMMAND, DISABLED


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
        self.centos_button = Button(master, text="YUM", state=DISABLED, command=self.centos, bg='purple', font='white')
        self.centos_button.grid(row=3,column=0,sticky=E,pady=10,padx=10)
#****Exit button****
        self.close_button = Button(master, text="Exit", command=master.quit, bg='red', font='white')
        self.close_button.grid(columnspan=2,sticky=W+E+S+N,pady=5,padx=10)

#define: APT function
    def APT(self):
        print("Now installing using apt-get!")
        update1 = subprocess.run(['sudo', 'apt-get', 'update'], shell=False)
        update01 = subprocess.run(['sudo', 'apt-get', 'upgrade', '-y'], shell=False, stdout=subprocess.PIPE)
        print (update01.stderr, update01.stdout)
        while update1 and update01 == 0:
            print ('System Updated, Now getting applications!!')
            print ('system upgraded getting applications!!!')
            import APT_script
            importing = subprocess.Popen(args=['*/./APT_script'],stdout=subprocess.PIPE,shell=False, text=True)
            print(importing.stdout)
            print(importing.stderr)
            new_var = 1
            if importing == new_var:
                root.mainloop()
            else:
                continue
           # importing.stdout.close()
        else:
            if update1 and update01 == 1:
                print(update1.stderr)
                print(update01.stderr)
                print('I broke here!!')

#define: ARCH function
    def arch(self):
        print ('Now installing Using Pacman')
        timer = time.sleep(1)
        timer = True
        if timer:
          time.sleep(2)
          print('script imported')
          time.sleep(2)
          print('Running Script Please Wait... ')
          add = time.sleep(5)
          import pacman_s
          if add:
              time.sleep(1)
              root.mainloop()
          else:
              exit

          #r = subprocess.Popen(args=['*/./pacman_script.py'],stdout=subprocess.PIPE,shell=False)
          #run = subprocess.run(['*/./pacman_s'], stdout=subprocess.PIPE, shell=False, text=True)
         # print(r.stdout)
        #else:
        #break

#################################################
   # def arch(self):
   #     print("Now installing using pacman!")
   #     update2 = subprocess.run(['sudo', 'pacman', '-Syu'], stdout=subprocess.PIPE, shell=False, text=True)
   #     while update2:
   #         print(update2.stdout)
   #         time.sleep(1)
   #         print ('system updated getting applications!!!')
   #         import pacman_script
   #         importing = subprocess.run(args=['*/./pacman_script'],stdout=subprocess.PIPE,shell=False, text=True)
   #         
   #         print (importing.returncode)
   #         importing.stdout.close()
   #         if importing == "None":
   #             root.mainloop()
   #         else:
   #             continue
 

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
