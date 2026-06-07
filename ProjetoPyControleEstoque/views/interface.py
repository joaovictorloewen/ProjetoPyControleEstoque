import tkinter as tk
from tkinter import ttk, messagebox

from models import (
    cadastrar_produto,
    listar_produtos,
    entrada_produto,
    saida_produto,
    excluir_produto,
    editar_produto
)

from views.dashboard import Dashboard
from views.historico import HistoricoWindow


class Interface:

    def __init__(self, root):

        self.root = root

        self.root.title("Controle de Estoque")
        self.root.geometry("1100x650")

        self.modo_edicao = False
        self.produto_editando = None

        self.dashboard = Dashboard(self.root)

        self.criar_componentes()

        self.atualizar_tabela()

    def criar_componentes(self):

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # =====================
        # CADASTRO
        # =====================

        tk.Label(
            frame,
            text="Produto"
        ).grid(row=0, column=0)

        self.nome_entry = tk.Entry(
            frame,
            width=20
        )
        self.nome_entry.grid(
            row=0,
            column=1
        )

        tk.Label(
            frame,
            text="Quantidade"
        ).grid(row=0, column=2)

        self.qtd_entry = tk.Entry(
            frame,
            width=10
        )
        self.qtd_entry.grid(
            row=0,
            column=3
        )

        tk.Label(
            frame,
            text="Preço"
        ).grid(row=0, column=4)

        self.preco_entry = tk.Entry(
            frame,
            width=10
        )
        self.preco_entry.grid(
            row=0,
            column=5
        )

        tk.Label(
            frame,
            text="Estoque Mínimo"
        ).grid(row=0, column=6)

        self.minimo_entry = tk.Entry(
            frame,
            width=10
        )
        self.minimo_entry.grid(
            row=0,
            column=7
        )

        self.btn_cadastrar = tk.Button(
            frame,
            text="Cadastrar",
            command=self.cadastrar
        )

        self.btn_cadastrar.grid(
            row=0,
            column=8,
            padx=10
        )

        # =====================
        # BUSCA
        # =====================

        tk.Label(
            frame,
            text="Buscar"
        ).grid(
            row=1,
            column=0,
            pady=10
        )

        self.busca_entry = tk.Entry(
            frame,
            width=20
        )

        self.busca_entry.grid(
            row=1,
            column=1
        )

        tk.Button(
            frame,
            text="Pesquisar",
            command=self.pesquisar
        ).grid(
            row=1,
            column=2
        )

        tk.Button(
            frame,
            text="Mostrar Todos",
            command=self.atualizar_tabela
        ).grid(
            row=1,
            column=3
        )

        # =====================
        # TABELA
        # =====================

        self.tabela = ttk.Treeview(
            self.root,
            columns=(
                "ID",
                "Nome",
                "Quantidade",
                "Preço",
                "Mínimo"
            ),
            show="headings"
        )

        self.tabela.heading(
            "ID",
            text="ID"
        )

        self.tabela.heading(
            "Nome",
            text="Nome"
        )

        self.tabela.heading(
            "Quantidade",
            text="Quantidade"
        )

        self.tabela.heading(
            "Preço",
            text="Preço"
        )

        self.tabela.heading(
            "Mínimo",
            text="Mínimo"
        )

        self.tabela.column(
            "ID",
            width=60
        )

        self.tabela.column(
            "Nome",
            width=300
        )

        self.tabela.column(
            "Quantidade",
            width=120
        )

        self.tabela.column(
            "Preço",
            width=120
        )

        self.tabela.column(
            "Mínimo",
            width=120
        )

        self.tabela.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.tabela.tag_configure(
            "baixo",
            background="#ffcccc"
        )

        # =====================
        # MOVIMENTAÇÃO
        # =====================

        frame_mov = tk.Frame(self.root)
        frame_mov.pack(
            pady=10
        )

        tk.Label(
            frame_mov,
            text="Quantidade"
        ).grid(
            row=0,
            column=0
        )

        self.mov_entry = tk.Entry(
            frame_mov,
            width=10
        )

        self.mov_entry.grid(
            row=0,
            column=1
        )

        tk.Button(
            frame_mov,
            text="Entrada",
            command=self.entrada
        ).grid(
            row=0,
            column=2,
            padx=5
        )

        tk.Button(
            frame_mov,
            text="Saída",
            command=self.saida
        ).grid(
            row=0,
            column=3,
            padx=5
        )

        tk.Button(
            frame_mov,
            text="Excluir Produto",
            command=self.excluir
        ).grid(
            row=0,
            column=4,
            padx=5
        )

        tk.Button(
            frame_mov,
            text="Histórico",
            command=self.abrir_historico
        ).grid(
            row=0,
            column=5,
            padx=5
        )

        tk.Button(
            frame_mov,
            text="Editar Produto",
            command=self.carregar_produto
        ).grid(
            row=0,
            column=6,
            padx=5
        )

    def cadastrar(self):

        try:

            nome = self.nome_entry.get()

            quantidade = int(
                self.qtd_entry.get()
            )

            preco = float(
                self.preco_entry.get()
            )

            minimo = int(
                self.minimo_entry.get()
            )

            if self.modo_edicao:

                editar_produto(
                    self.produto_editando,
                    nome,
                    quantidade,
                    preco,
                    minimo
                )

                self.modo_edicao = False
                self.produto_editando = None

                self.btn_cadastrar.config(
                    text="Cadastrar"
                )

                messagebox.showinfo(
                    "Sucesso",
                    "Produto atualizado!"
                )

            else:

                cadastrar_produto(
                    nome,
                    quantidade,
                    preco,
                    minimo
                )

                messagebox.showinfo(
                    "Sucesso",
                    "Produto cadastrado!"
                )

            self.limpar_campos()

            self.atualizar_tabela()

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )

    def limpar_campos(self):

        self.nome_entry.delete(0, tk.END)
        self.qtd_entry.delete(0, tk.END)
        self.preco_entry.delete(0, tk.END)
        self.minimo_entry.delete(0, tk.END)

    def atualizar_tabela(self):

        for item in self.tabela.get_children():
            self.tabela.delete(item)

        produtos = listar_produtos()

        for produto in produtos:

            tag = ""

            if produto["quantidade"] <= produto["minimo"]:
                tag = "baixo"

            self.tabela.insert(
                "",
                tk.END,
                values=(
                    produto["id"],
                    produto["nome"],
                    produto["quantidade"],
                    f"R$ {produto['preco']:.2f}",
                    produto["minimo"]
                ),
                tags=(tag,)
            )

        self.dashboard.atualizar()

    def pesquisar(self):

        texto = self.busca_entry.get().lower()

        for item in self.tabela.get_children():
            self.tabela.delete(item)

        for produto in listar_produtos():

            if texto in produto["nome"].lower():

                tag = ""

                if produto["quantidade"] <= produto["minimo"]:
                    tag = "baixo"

                self.tabela.insert(
                    "",
                    tk.END,
                    values=(
                        produto["id"],
                        produto["nome"],
                        produto["quantidade"],
                        f"R$ {produto['preco']:.2f}",
                        produto["minimo"]
                    ),
                    tags=(tag,)
                )

    def obter_id_selecionado(self):

        item = self.tabela.selection()

        if not item:
            return None

        dados = self.tabela.item(item)

        return int(
            dados["values"][0]
        )

    def carregar_produto(self):

        produto_id = self.obter_id_selecionado()

        if not produto_id:

            messagebox.showwarning(
                "Aviso",
                "Selecione um produto."
            )

            return

        for produto in listar_produtos():

            if produto["id"] == produto_id:

                self.limpar_campos()

                self.nome_entry.insert(
                    0,
                    produto["nome"]
                )

                self.qtd_entry.insert(
                    0,
                    produto["quantidade"]
                )

                self.preco_entry.insert(
                    0,
                    produto["preco"]
                )

                self.minimo_entry.insert(
                    0,
                    produto["minimo"]
                )

                self.produto_editando = produto_id
                self.modo_edicao = True

                self.btn_cadastrar.config(
                    text="Salvar Alterações"
                )

                break

    def entrada(self):

        try:

            produto_id = self.obter_id_selecionado()

            if not produto_id:

                messagebox.showwarning(
                    "Aviso",
                    "Selecione um produto."
                )

                return

            quantidade = int(
                self.mov_entry.get()
            )

            entrada_produto(
                produto_id,
                quantidade
            )

            self.mov_entry.delete(
                0,
                tk.END
            )

            self.atualizar_tabela()

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )

    def saida(self):

        try:

            produto_id = self.obter_id_selecionado()

            if not produto_id:

                messagebox.showwarning(
                    "Aviso",
                    "Selecione um produto."
                )

                return

            quantidade = int(
                self.mov_entry.get()
            )

            saida_produto(
                produto_id,
                quantidade
            )

            self.mov_entry.delete(
                0,
                tk.END
            )

            self.atualizar_tabela()

        except Exception as erro:

            messagebox.showerror(
                "Erro",
                str(erro)
            )

    def excluir(self):

        produto_id = self.obter_id_selecionado()

        if not produto_id:

            messagebox.showwarning(
                "Aviso",
                "Selecione um produto."
            )

            return

        resposta = messagebox.askyesno(
            "Confirmação",
            "Deseja excluir o produto?"
        )

        if resposta:

            excluir_produto(
                produto_id
            )

            self.atualizar_tabela()

    def abrir_historico(self):

        HistoricoWindow()