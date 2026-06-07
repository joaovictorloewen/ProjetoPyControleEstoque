import json
import os
from datetime import datetime

ARQ_PRODUTOS = "data/produtos.json"
ARQ_MOVIMENTOS = "data/movimentacoes.json"
ARQ_USUARIOS = "data/usuarios.json"


# ==========================
# UTILITÁRIOS
# ==========================

def carregar_json(caminho):
    if not os.path.exists(caminho):
        return []

    with open(caminho, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_json(caminho, dados):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(
            dados,
            arquivo,
            indent=4,
            ensure_ascii=False
        )


# ==========================
# LOGIN
# ==========================

def validar_login(usuario, senha):
    usuarios = carregar_json(ARQ_USUARIOS)

    for usuario_bd in usuarios:
        if (
            usuario_bd["usuario"] == usuario
            and usuario_bd["senha"] == senha
        ):
            return True

    return False


# ==========================
# PRODUTOS
# ==========================

def gerar_id():
    produtos = carregar_json(ARQ_PRODUTOS)

    if not produtos:
        return 1

    return max(produto["id"] for produto in produtos) + 1


def cadastrar_produto(nome, quantidade, preco, minimo):
    produtos = carregar_json(ARQ_PRODUTOS)

    novo_produto = {
        "id": gerar_id(),
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco,
        "minimo": minimo
    }

    produtos.append(novo_produto)

    salvar_json(ARQ_PRODUTOS, produtos)


def listar_produtos():
    return carregar_json(ARQ_PRODUTOS)


def buscar_produtos(texto):
    produtos = listar_produtos()

    return [
        produto
        for produto in produtos
        if texto.lower() in produto["nome"].lower()
    ]


def excluir_produto(produto_id):
    produtos = listar_produtos()

    produtos = [
        produto
        for produto in produtos
        if produto["id"] != produto_id
    ]

    salvar_json(ARQ_PRODUTOS, produtos)


def editar_produto(produto_id, nome, quantidade, preco, minimo):
    produtos = listar_produtos()

    for produto in produtos:
        if produto["id"] == produto_id:

            produto["nome"] = nome
            produto["quantidade"] = quantidade
            produto["preco"] = preco
            produto["minimo"] = minimo

            break

    salvar_json(ARQ_PRODUTOS, produtos)


# ==========================
# MOVIMENTAÇÕES
# ==========================

def registrar_movimentacao(produto, tipo, quantidade):
    movimentacoes = carregar_json(ARQ_MOVIMENTOS)

    movimentacoes.append({
        "produto": produto,
        "tipo": tipo,
        "quantidade": quantidade,
        "data": datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )
    })

    salvar_json(
        ARQ_MOVIMENTOS,
        movimentacoes
    )


def entrada_produto(produto_id, quantidade):
    produtos = listar_produtos()

    for produto in produtos:
        if produto["id"] == produto_id:

            produto["quantidade"] += quantidade

            registrar_movimentacao(
                produto["nome"],
                "ENTRADA",
                quantidade
            )

            break

    salvar_json(
        ARQ_PRODUTOS,
        produtos
    )


def saida_produto(produto_id, quantidade):
    produtos = listar_produtos()

    for produto in produtos:
        if produto["id"] == produto_id:

            if produto["quantidade"] >= quantidade:

                produto["quantidade"] -= quantidade

                registrar_movimentacao(
                    produto["nome"],
                    "SAÍDA",
                    quantidade
                )

            break

    salvar_json(
        ARQ_PRODUTOS,
        produtos
    )


def listar_movimentacoes():
    return carregar_json(
        ARQ_MOVIMENTOS
    )


# ==========================
# DASHBOARD
# ==========================

def dashboard():
    produtos = listar_produtos()

    total_produtos = len(produtos)

    total_itens = sum(
        produto["quantidade"]
        for produto in produtos
    )

    valor_total = sum(
        produto["quantidade"] * produto["preco"]
        for produto in produtos
    )

    estoque_baixo = len([
        produto
        for produto in produtos
        if produto["quantidade"] <= produto["minimo"]
    ])

    return {
        "produtos": total_produtos,
        "itens": total_itens,
        "valor": valor_total,
        "baixo": estoque_baixo
    }