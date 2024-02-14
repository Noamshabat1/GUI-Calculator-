import math
import numpy as np
from tkinter import *

expression = ""


def press(item):
    global expression
    expression = expression + str(item)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""

    except:
        equation.set("Error!")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="light gray")
    gui.title("Noam's second Calculator!")
    gui.geometry("365x475")
    equation = StringVar()
    expression_input = Entry(gui, textvariable=equation, width=33)
    expression_input.grid(columnspan=5, ipadx=80)

    button_1 = Button(gui, text=' 1 ', fg='white', bg='black',
                      font="Courier 9 bold",
                      command=lambda: press(1), height=4, width=9)
    button_1.grid(row=2, column=0)

    button_2 = Button(gui, text=' 2 ', fg='white', bg='black',
                      font="Courier 9 bold",
                      command=lambda: press(2), height=4, width=9)
    button_2.grid(row=2, column=1)

    button_3 = Button(gui, text=' 3 ', fg='white', bg='black',
                      font="Courier 9 bold",
                      command=lambda: press(3), height=4, width=9)
    button_3.grid(row=2, column=2)

    button_4 = Button(gui, text=' 4 ', fg='white', bg='black',
                      font="Courier 9 bold",
                      command=lambda: press(4), height=4, width=9)
    button_4.grid(row=3, column=0)

    button_5 = Button(gui, text=' 5 ', fg='white', bg='black',
                      font="Courier 9 bold",
                      command=lambda: press(5), height=4, width=9)
    button_5.grid(row=3, column=1)

    button_6 = Button(gui, text=' 6 ', fg='white', bg='black',
                      font="Courier 9 bold",
                      command=lambda: press(6), height=4, width=9)
    button_6.grid(row=3, column=2)

    button_7 = Button(gui, text=' 7 ', fg='white', bg='black',
                      font="Courier 9 bold",
                      command=lambda: press(7), height=4, width=9)
    button_7.grid(row=4, column=0)

    button_8 = Button(gui, text=' 8 ', fg='white', bg='black',
                      font="Courier 9 bold",
                      command=lambda: press(8), height=4, width=9)
    button_8.grid(row=4, column=1)

    button_9 = Button(gui, text=' 9 ', fg='white', bg='black',
                      font="Courier 9 bold",
                      command=lambda: press(9), height=4, width=9)
    button_9.grid(row=4, column=2)

    button_0 = Button(gui, text=' 0 ', fg='white', bg='black',
                      font="Courier 9 bold",
                      command=lambda: press(0), height=4, width=9)
    button_0.grid(row=5, column=0)

    button_PI = Button(gui, text=' PI ', fg='white', bg='black',
                       font="Courier 9 bold",
                       command=lambda: press(math.pi), height=4, width=9)
    button_PI.grid(row=6, column=0)

    button_E = Button(gui, text=' e ', fg='white', bg='black',
                      font="Courier 9 bold",
                      command=lambda: press(math.e), height=4, width=9)
    button_E.grid(row=6, column=1)

    plus = Button(gui, text=' + ', fg='black', bg='green',
                  font="Courier 9 bold",
                  command=lambda: press("+"), height=4, width=9)
    plus.grid(row=2, column=3, rowspan=1)  # ipady=1, ipadx=1)

    minus = Button(gui, text=' - ', fg='black', bg='green',
                   font="Courier 9 bold",
                   command=lambda: press("-"), height=4, width=9)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='green',
                      font="Courier 9 bold",
                      command=lambda: press("*"), height=4, width=9)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='green',
                    font="Courier 9 bold",
                    command=lambda: press("/"), height=4, width=9)
    divide.grid(row=5, column=3)

    sqrt_root = Button(gui, text=' ^0.5 ', fg='black', bg='green',
                       font="Courier 9 bold",
                       command=lambda: press("**0.5"), height=4, width=9)
    sqrt_root.grid(row=7, column=2)

    power = Button(gui, text=' ^ ', fg='black', bg='green',
                   font="Courier 9 bold",
                   command=lambda: press("**"), height=4, width=9)
    power.grid(row=6, column=3)

    equal = Button(gui, text=' = ', fg='black', bg='dark blue',
                   font="Courier 9 bold",
                   command=equalpress, height=4, width=20)
    equal.grid(row=7, column=3, columnspan=2)

    clear = Button(gui, text='Clear', fg='white', bg='gray',
                   font="Courier 9 bold",
                   command=clear, height=4, width=9)
    clear.grid(row=2, column=4)

    Decimal_point = Button(gui, text='.', fg='white', bg='black',
                           font="Courier 9 bold",
                           command=lambda: press('.'), height=4, width=9)
    Decimal_point.grid(row=6, column=2)

    button_for_sin = Button(gui, text=' sin( ) ', fg='black', bg='yellow',
                            font="Courier 9 bold",
                            command=lambda: press(math.sin(int(expression))),
                            height=4, width=9)
    button_for_sin.grid(row=3, column=4)

    button_for_cos = Button(gui, text=' cos( ) ', fg='black', bg='yellow',
                            font="Courier 9 bold",
                            command=lambda: press(math.cos(int(expression))),
                            height=4, width=9)
    button_for_cos.grid(row=4, column=4)

    button_for_tan = Button(gui, text=' tan( ) ', fg='black', bg='yellow',
                            font="Courier 9 bold",
                            command=lambda: press(math.tan(int(expression))),
                            height=4, width=9)
    button_for_tan.grid(row=5, column=4)

    button_for_log = Button(gui, text=' log( ) ', fg='black', bg='yellow',
                            font="Courier 9 bold",
                            command=lambda: press(math.log(int(expression))),
                            height=4, width=9)
    button_for_log.grid(row=6, column=4)

    button_open_Parentheses = Button(gui, text=' ( ', fg='white', bg='black',
                                     font="Courier 9 bold",
                                     command=lambda: press("("), height=4,
                                     width=9)
    button_open_Parentheses.grid(row=5, column=1)

    button_close_Parentheses = Button(gui, text=' ) ', fg='white', bg='black',
                                      font="Courier 9 bold",
                                      command=lambda: press(")"), height=4,
                                      width=9)
    button_close_Parentheses.grid(row=5, column=2)

    button_Percent = Button(gui, text=' % ', fg='black', bg='green',
                            font="Courier 9 bold",
                            command=lambda: press("%"), height=4,
                            width=9)
    button_Percent.grid(row=7, column=1)

    button_Best_num = Button(gui, text='Best num', fg='white', bg='black',
                             font="Courier 9 bold",
                             command=lambda: press(73), height=4,
                             width=9)
    button_Best_num.grid(row=7, column=0)

    gui.mainloop()
