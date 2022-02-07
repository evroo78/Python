from tkinter import *
from tkinter.colorchooser import *
root = Tk()
c = askcolor(parent=root,initialcolor=(255,255,255))
print(c)
