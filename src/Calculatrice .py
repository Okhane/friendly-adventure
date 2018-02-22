"""

Application Calculatrice avec tests de l'interface graphique intégrés

Par Pier-Olivier Vermette et
    Jean-Sébastien St-Pierre

"""

from tkinter import *
import math
import time
import random
import mock
from mock import MagicMock


class calc:
    flag = 0


    # Math evaluation of entry

    def evaluateExpression(self, answer):
        return round(eval(answer), 2)

    def egale(self):
        try:
            self.value = self.evaluateExpression(self.e.get())
        except ZeroDivisionError:
            self.e.delete(0, END)
            self.e.insert(0, 'Entree invalide')
            self.flag = 1

        else:
            self.e.delete(0, END)
            self.e.insert(0, format(self.value, '.2f'))
            self.flag = 1

    def test(event):
        calc.egale(obj)

    # Delete display
    def clearall(self):
        self.e.delete(0, END)

    # Delete last character
    def clear_1(self):
        self.txt = self.e.get()[:-1]
        self.e.delete(0, END)
        self.e.insert(0, self.txt)

    def action(self, val):
        if self.flag == 1:
            self.clearall()
            self.flag = 0
        self.e.insert(END, val)

    # GUI init
    def __init__(self, master):
        root.resizable(0, 0)
        self.flag = 0
        master.title('Calculatrice')
        master.geometry()
        self.e = Entry(master, width=18, justify=RIGHT, font=("Arial", 30))
        self.e.grid(columnspan=5, pady=5, sticky=W)
        self.e.focus_set()

        # bUILDING BUTTONS
        B0 = Button(master, font=("Arial", 13), text="=", width=10, height=3, command=lambda: self.egale())
        B0.grid(row=7, column=0, sticky=N + S + E + W, columnspan=4)
        B1 = Button(master, font=("Arial", 13), text="±", width=10, height=3, command=lambda: self.action('-'))
        B1.grid(row=6, column=1, sticky=N + S + E + W)
        B2 = Button(master, font=("Arial", 13), text='AC', width=10, height=3, command=lambda: self.clearall())
        B2.grid(row=6, column=0, sticky=N + S + E + W)
        B3 = Button(master, font=("Arial", 13), text='DEL', width=10, height=3, command=lambda: self.clear_1())
        B3.grid(row=5, column=0, sticky=N + S + E + W)
        B4 = Button(master, font=("Arial", 13), text="+", width=10, height=3, command=lambda: self.action('+'))
        B4.grid(row=4, column=3, sticky=N + S + E + W)
        B5 = Button(master, font=("Arial", 13), text="*", width=10, height=3, command=lambda: self.action('*'))
        B5.grid(row=2, column=3, sticky=N + S + E + W)
        B6 = Button(master, font=("Arial", 13), text="-", width=10, height=3, command=lambda: self.action('-'))
        B6.grid(row=3, column=3, sticky=N + S + E + W)
        B7 = Button(master, font=("Arial", 13), text="/", width=10, height=3, command=lambda: self.action('/'))
        B7.grid(row=5, column=3, sticky=N + S + E + W)
        B8 = Button(master, font=("Arial", 13), text="7", width=10, height=3, bg='white',
                    command=lambda: self.action('7'))
        B8.grid(row=2, column=0, sticky=N + S + E + W)
        B9 = Button(master, font=("Arial", 13), text="8", width=10, height=3, bg='white',
                    command=lambda: self.action(8))
        B9.grid(row=2, column=1, sticky=N + S + E + W)
        B10 = Button(master, font=("Arial", 13), text="9", width=10, height=3, bg='white',
                     command=lambda: self.action(9))
        B10.grid(row=2, column=2, sticky=N + S + E + W)
        B11 = Button(master, font=("Arial", 13), text="4", width=10, height=3, bg='white',
                     command=lambda: self.action(4))
        B11.grid(row=3, column=0, sticky=N + S + E + W)
        B12 = Button(master, font=("Arial", 13), text="5", width=10, height=3, bg='white',
                     command=lambda: self.action(5))
        B12.grid(row=3, column=1, sticky=N + S + E + W)
        B13 = Button(master, font=("Arial", 13), text="6", width=10, height=3, bg='white',
                     command=lambda: self.action(6))
        B13.grid(row=3, column=2, sticky=N + S + E + W)
        B14 = Button(master, font=("Arial", 13), text="1", width=10, height=3, bg='white',
                     command=lambda: self.action(1))
        B14.grid(row=4, column=0, sticky=N + S + E + W)
        B15 = Button(master, font=("Arial", 13), text="2", width=10, height=3, bg='white',
                     command=lambda: self.action(2))
        B15.grid(row=4, column=1, sticky=N + S + E + W)
        B16 = Button(master, font=("Arial", 13), text="3", width=10, height=3, bg='white',
                     command=lambda: self.action(3))
        B16.grid(row=4, column=2, sticky=N + S + E + W)

        B17 = Button(master, font=("Arial", 13), text="0", width=10, height=3, bg='white',
                    command=lambda: self.action(0))
        B17.grid(row=5, column=1, sticky=N + S + E + W)
        B18 = Button(master, font=("Arial", 13), text=".", width=10, height=3,
                     command=lambda: self.action('.'))
        B18.grid(row=5, column=2, sticky=N + S + E + W)
        B19 = Button(master, font=("Arial", 13), text="(", width=10, height=3,
                     command=lambda: self.action('('))
        B19.grid(row=6, column=2, sticky=N + S + E + W)
        B20 = Button(master, font=("Arial", 13), text=")", width=10, height=3,
                     command=lambda: self.action(')'))
        B20.grid(row=6, column=3, sticky=N + S + E + W)









# Creating object + mainloop
root = Tk()
obj = calc(root)
root.bind("<Return>", lambda event: calc.test(event))  # Attribue la fonction 'egale' a la touche Enter
root.mainloop()


