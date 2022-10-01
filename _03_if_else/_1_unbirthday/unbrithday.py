from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    birthday = simpledialog.askstring(title="birthday?", prompt="When is your birthday?")
    if birthday == '9/30':
        messagebox.showinfo(title="amazing!", message="Happy birthday!")

