from tkinter import *
from tkinter.messagebox import * 
def f():
  if (askyesno (title="Запит", message="Перенести дані?")):
    l['text'] = e.get()
    e.delete(0, END)
root = Tk()
e = Entry()
l = Label()
b = Button(text = 'Переписати', command = f)
e.pack()
b.pack()
l.pack()
root.mainloop()
