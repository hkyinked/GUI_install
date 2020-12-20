########################
import subprocess
from typing import Counter
########################

my_lines= []
Counter = 0
with open("bash_cpy", 'r') as f:
        f_contents = f.readlines()
        for line in f_contents:
            line = str(line).rstrip()
            line = str(line).strip()
            my_lines.append(line)
        for element in my_lines:
            Counter += 1
            #print(element, str(Counter), end='')
            key_value = "export PS1="
            if key_value in element:
                print(element)
                print ('Success!')
                print(str(Counter))
                success=True
                if success:
                    message='This worked!'
                    print (message)
            #        os.write(f , 'r+', message)
            else:
                continue
                print(element,Counter, '\t', 'Failed')
                Counter +1





#        f.readlines()
#        for lines in f.readlines:
#            if (lines in f.readlines == ('export PS1') or ('PS1=')):
#                file = 'This works'
#                #file = ('export PS1="\[$(tput bold)\]\[\033[38;5;128m\]\u\[$(tput sgr0)\] \[$(tput sgr0)\]\[\033[38;5;11m\]>>\[$(tput sgr0)\] \[$(tput sgr0)\]\[$(tput bold)\]\[\033[38;5;166m\]\w\[$(tput sgr0)\]\n\[$(tput sgr0)\]\[$(tput bold)\]\[\033[38;5;1m\]\\$\[$(tput sgr0)\]"')
#                f.write(file)
#                f.close()
#            print(f)
#        cats = subprocess.run('cat', '~/bashrc_cpy')
#print(cats)