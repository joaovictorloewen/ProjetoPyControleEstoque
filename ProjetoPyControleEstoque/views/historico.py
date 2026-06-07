import tkinter as tk
from tkinter import ttk

from models import listar_movimentacoes


class HistoricoWindow:

    def __init__(self):

        self.janela = tk.Toplevel()

        self.janela.title(
            "Histórico de Movimentações"
        )

        self.janela.geometry(
            "800x400"
        )

        self.tabela = ttk.Treeview(
            self.janela,
            columns=(
                "Produto",
                "Tipo",
                "Quantidade",
                "Data"
            ),
            show="headings"
        )

        self.tabela.heading(
            "Produto",
            text="Produto"
        )

        self.tabela.heading(
            "Tipo",
            text="Tipo"
        )

        self.tabela.heading(
            "Quantidade",
            text="Quantidade"
        )

        self.tabela.heading(
            "Data",
            text="Data"
        )

        self.tabela.pack(
            fill="both",
            expand=True
        )

        self.carregar()

    def carregar(self):

        for item in self.tabela.get_children():
            self.tabela.delete(item)

        for mov in listar_movimentacoes():

            self.tabela.insert(
                "",
                tk.END,
                values=(
                    mov["produto"],
                    mov["tipo"],
                    mov["quantidade"],
                    mov["data"]
                )
            )