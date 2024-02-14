import math
from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Noam's Advanced Calculator")
        master.configure(background="light blue")
        master.geometry("450x650")

        self.expression = ""
        self.equation = StringVar()

        self.create_widgets()

    def create_widgets(self):
        expression_input = Entry(self.master, textvariable=self.equation, font=('Arial', 18), width=20, borderwidth=5, relief='sunken')
        expression_input.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        buttons = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2),
            ('0', 5, 0), ('.', 5, 1), ('+', 5, 2),
            ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
            ('(', 6, 0), (')', 6, 1), ('%', 6, 2)
        ]

        for (text, row, col) in buttons:
            Button(self.master, text=text, fg='white', bg='dark blue', font=('Arial', 12),
                   command=lambda b=text: self.press(b), height=2, width=7).grid(row=row, column=col, sticky="nsew")

        advanced_buttons = [
            ('sin', lambda: self.scientific_operation(math.sin), 7, 0),
            ('cos', lambda: self.scientific_operation(math.cos), 7, 1),
            ('tan', lambda: self.scientific_operation(math.tan), 7, 2),
            ('log', lambda: self.scientific_operation(math.log), 7, 3),
            ('√', lambda: self.scientific_operation(math.sqrt), 8, 0),
            ('^', lambda: self.press('**'), 8, 1),
            ('π', lambda: self.press(math.pi), 8, 2),
            ('e', lambda: self.press(math.e), 8, 3),
            ('←', self.backspace, 9, 3)
        ]

        for (text, func, row, col) in advanced_buttons:
            Button(self.master, text=text, fg='black', bg='orange', font=('Arial', 12),
                   command=func, height=2, width=7).grid(row=row, column=col, sticky="nsew")

        Button(self.master, text='=', fg='black', bg='green', font=('Arial', 12),
               command=self.equalpress, height=2, width=15).grid(row=9, column=0, columnspan=3, sticky="nsew")

        Button(self.master, text='Clear', fg='white', bg='red', font=('Arial', 12),
               command=self.clear, height=2, width=15).grid(row=6, column=3, sticky="nsew")

        for i in range(10):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

    def press(self, item):
        self.expression += str(item)
        self.equation.set(self.expression)

    def scientific_operation(self, func):
        try:
            result = str(func(float(eval(self.expression))))
            self.equation.set(result)
            self.expression = result
        except Exception:
            self.equation.set("Error")
            self.expression = ""

    def backspace(self):
        self.expression = self.expression[:-1]
        self.equation.set(self.expression)

    def equalpress(self):
        try:
            total = str(eval(self.expression))
            self.equation.set(total)
            self.expression = total
        except Exception:
            self.equation.set("Error")
            self.expression = ""

    def clear(self):
        self.expression = ""
        self.equation.set("")

if __name__ == "__main__":
    root = Tk()
    my_calculator = Calculator(root)
    root.mainloop()
