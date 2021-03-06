# аналог блокнота

from tkinter import *
from tkinter.filedialog import * 
def inText():
  name = askopenfilename()
  if (str(name)!="()"): # використано для того, щоб уникнути зауважень (помилок) при натисканні клавіш з написом Cancel
    f = open(name)
    s = f.read()
    t.delete(1.0,END)
    t.insert(1.0,s)
    f.close()
 
def outText():
  name = asksaveasfilename(
    filetypes = (
    ("TXT files", "* .txt"),
    ("HTML files", "* .html; *. htm"),
    ( "All files", "*. *")))
  if (str(name)!=""):  # використано для того, щоб уникнути зауважень (помилок) при натисканні клавіш з написом Cancel
    f = open(name, 'w')
    s = t.get(1.0, END)
    f.write(s)
    f.close()
 
root = Tk()
t = Text(width = 30, height = 5)
t.grid (columnspan = 2)
b1 = Button(text = "Відкрити", command = inText)
b2 = Button(text = "Зберегти", command = outText)
b1.grid (row = 1, sticky = E)
b2.grid (row = 1, column = 1, sticky = W)
root.mainloop()
