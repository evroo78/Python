from tkinter import *
from tkinter.messagebox import * 
def f():
  s = e.get()
  if s.isdigit():
    e.delete(0, END)
    l['text'] = s
  else:
    showerror("Помилка","Потрібно ввести десятковий запис числа!")
    showinfo("Повідомлення","Потрібно ввести десятковий запис числа!")
    showwarning("Зауваження","Потрібно ввести десятковий запис числа!")
root = Tk()
e = Entry()
l = Label()
b = Button(text = 'Переписати', command = f)
e.pack()
b.pack()
l.pack()
root.mainloop()
