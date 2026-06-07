import tkinter as tk

from views.login import LoginWindow
from views.interface import Interface


def abrir_sistema():

    root = tk.Tk()

    Interface(root)

    root.mainloop()


login_root = tk.Tk()

LoginWindow(
    login_root,
    abrir_sistema
)

login_root.mainloop()