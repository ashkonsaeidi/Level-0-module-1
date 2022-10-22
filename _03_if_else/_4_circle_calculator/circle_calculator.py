from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr

    radius = simpledialog.askstring(title="Prompt", prompt="Give me the radius for a circle")
    circle = simpledialog.askstring(title="Prompt", prompt="Calculate the area or circumference of a circle")
    if circle == "area":
        math.pi*(radius**2)
    if circle == "circumference":
        2*math.pi*radius


