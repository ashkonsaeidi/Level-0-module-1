import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    jack=turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title="What shape", prompt="What shape do you want me to draw")
    # Draw the shape requested by the user using if-elif-else statements
    if shape == "Circle":
        jack.circle(radius=100)
    if shape == "Square":
        for i in range(4):
            jack.forward(40)
            jack.right(90)
    # Call the turtle .done() method
            jack.done()
