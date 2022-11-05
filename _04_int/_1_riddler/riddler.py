"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
from tkinter import messagebox, simpledialog, Tk
import #riddle

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    riddle = simpledialog.askstring(title="Riddle", prompt="I make two people out of one. What am I?")
    if riddle == "A mirror":
        messagebox.showinfo(Title=":o", message="Correct!")
    if riddle != "A mirror":
        messagebox.showinfo(Title="Nuh uh", prompt="Incorrect, u suck)"
r
