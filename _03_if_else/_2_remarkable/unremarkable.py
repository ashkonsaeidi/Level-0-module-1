from tkinter import messagebox, simpledialog, Tk


if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    friend = simpledialog.askstring(title="Choose", prompt="Choose a student")
    if friend == 'ryan':
        messagebox.showinfo(title="Remarkable", message="Ryan is a tennis pro with a 16 UTR")

    if friend == 'josh':
        messagebox.showinfo(title="Remarkable", message="Josh is a grandmaster at chess")

    if friend == 'kyle':
        messagebox.showinfo(title="Remarkable", message="Kyle is very smart at math having 7 math olimpiad wins")


