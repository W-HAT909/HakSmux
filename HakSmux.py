# This For Setting HakSmux
import os

os.system("clear")
os.system("pkg install jp2a")
os.system("rm $HOME/../usr/etc/bash.bashrc")
os.system("mv bash.bashrc $HOME/../usr/etc")
os.system("mkdir $HOME/../usr/etc/HakSmuX")
os.system("mv * $HOME/../usr/etc/HakSmuX")
os.chdir(os.environ["HOME"]) 
os.system("login") 
