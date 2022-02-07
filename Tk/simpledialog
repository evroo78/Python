from tkinter import *
from tkinter.simpledialog import *
root = Tk()

a = askstring("Введення даних", "Ваше ім'я?",parent=root)
if (a!=None): print("Ваше ім'я ", a)
else:         print("Ви не знаєте свого імені?")

a = askinteger("Введення даних", "Скільки Вам повних років?",
    parent=root, minvalue=0, maxvalue=125)
if (a!=None): print("Ваш вік (у роках) ", a, ".")
else:         print("Ви не знаєте, скільки Вам років?")

a = askfloat("Введення даних", "Який Ваш ріст у метрах?",
    parent=root, minvalue=0.0, maxvalue=2.5)
if (a!=None): print("Ваш ріст ", a, " м.")
else:         print("Ви не знаєте, якого Ви зросту?")
