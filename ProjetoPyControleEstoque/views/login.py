import tkinter as tk
from tkinter import messagebox

from models import validar_login


class LoginWindow:

    def __init__(self, root, abrir_sistema):

        self.root = root
        self.abrir_sistema = abrir_sistema

        self.root.title("Login")
        self.root.geometry("350x200")
        self.root.resizable(False, False)

        self.criar_componentes()

    def criar_componentes(self):

        frame = tk.Frame(self.root)
        frame.pack(expand=True)

        tk.Label(
            frame,
            text="Usuário",
            font=("Arial", 10)
        ).grid(row=0, column=0, pady=10)

        self.usuario_entry = tk.Entry(
            frame,
            width=25
        )
        self.usuario_entry.grid(
            row=0,
            column=1
        )

        tk.Label(
            frame,
            text="Senha",
            font=("Arial", 10)
        ).grid(row=1, column=0, pady=10)

        self.senha_entry = tk.Entry(
            frame,
            show="*",
            width=25
        )

        self.senha_entry.grid(
            row=1,
            column=1
        )

        btn_login = tk.Button(
            frame,
            text="Entrar",
            width=15,
            command=self.login
        )

        btn_login.grid(
            row=2,
            column=0,
            columnspan=2,
            pady=15
        )

    def login(self):

        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()

        if validar_login(
            usuario,
            senha
        ):

            self.root.destroy()

            self.abrir_sistema()

        else:

            messagebox.showerror(
                "Erro",
                "Usuário ou senha inválidos."
            )