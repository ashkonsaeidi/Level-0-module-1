"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""
from tkinter import messagebox, simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    num1 = simpledialog.askinteger(title="ok", prompt="Give me 1 number")
    num2 = simpledialog.askinteger(title="ok", prompt="Give me another number")
    answer = simpledialog.askstring(title="ok", prompt="Would you like to subtract, divide, multiply, or add")
    if answer == "subtract":
       total=num1-num2
       print(str(total))
    if answer == "add":
        total=num1+num2
        print(str(total))
    if answer == "divide":
        total=num1/num2
        print(str(total))
    if answer == "multiply":
        total=num1*num2
        print(str(total))
