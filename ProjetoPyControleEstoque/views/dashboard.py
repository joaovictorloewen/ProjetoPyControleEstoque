import tkinter as tk

from models import dashboard


class Dashboard:

    def __init__(self, parent):

        self.frame = tk.Frame(parent)

        self.frame.pack(
            fill="x",
            padx=10,
            pady=10
        )

        self.card_produtos = tk.Label(
            self.frame,
            text="Produtos\n0",
            relief="groove",
            width=20,
            height=3
        )

        self.card_itens = tk.Label(
            self.frame,
            text="Itens\n0",
            relief="groove",
            width=20,
            height=3
        )

        self.card_valor = tk.Label(
            self.frame,
            text="Valor Total\nR$ 0,00",
            relief="groove",
            width=20,
            height=3
        )

        self.card_baixo = tk.Label(
            self.frame,
            text="Estoque Baixo\n0",
            relief="groove",
            width=20,
            height=3
        )

        self.card_produtos.pack(side="left", padx=5)
        self.card_itens.pack(side="left", padx=5)
        self.card_valor.pack(side="left", padx=5)
        self.card_baixo.pack(side="left", padx=5)

        self.atualizar()

    def atualizar(self):

        dados = dashboard()

        self.card_produtos.config(
            text=f"Produtos\n{dados['produtos']}"
        )

        self.card_itens.config(
            text=f"Itens\n{dados['itens']}"
        )

        self.card_valor.config(
            text=f"Valor Total\nR$ {dados['valor']:.2f}"
        )

        self.card_baixo.config(
            text=f"Estoque Baixo\n{dados['baixo']}"
        )