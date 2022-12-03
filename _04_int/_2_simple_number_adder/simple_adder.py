"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    num1 = simpledialog.askinteger(title="ok", prompt="Give me 1 number")
    num2 = simpledialog.askinteger(title="ok", prompt="Give me 1 number")
    total = num1+num2
    print(str(total))



