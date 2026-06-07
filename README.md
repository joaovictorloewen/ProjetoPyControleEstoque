# 📦 Sistema de Controle de Estoque em Python

## 📖 Sobre o Projeto

Este projeto é um sistema de controle de estoque desenvolvido em Python com interface gráfica utilizando Tkinter.

O objetivo do sistema é permitir o gerenciamento de produtos de forma simples e intuitiva, possibilitando o cadastro, edição, movimentação e consulta de itens armazenados em estoque.

Todos os dados são armazenados localmente em arquivos JSON, eliminando a necessidade de um banco de dados externo.

---

## 🚀 Funcionalidades

### 📋 Gestão de Produtos

* Cadastro de produtos
* Edição de produtos
* Exclusão de produtos
* Consulta de produtos cadastrados

### 📦 Controle de Estoque

* Entrada de produtos
* Saída de produtos
* Controle de estoque mínimo
* Destaque visual para produtos com estoque baixo

### 🔍 Pesquisa

* Busca de produtos por nome
* Atualização dinâmica da tabela

### 📊 Dashboard

* Quantidade total de produtos
* Total de itens em estoque
* Valor total do estoque
* Produtos com estoque abaixo do mínimo

### 📝 Histórico

* Registro de movimentações
* Data e hora das operações
* Consulta completa do histórico

### 💾 Persistência de Dados

* Armazenamento em arquivos JSON
* Não requer banco de dados
* Fácil backup e portabilidade

---

## 🛠️ Tecnologias Utilizadas

* Python 3
* Tkinter
* JSON
* OS
* Datetime

---

## 📁 Estrutura do Projeto

```text
ProjetoPyControleEstoque/
│
├── main.py
├── models.py
│
├── data/
│   ├── produtos.json
│   ├── movimentacoes.json
│   └── usuarios.json
│
└── views/
    ├── __init__.py
    ├── login.py
    ├── dashboard.py
    ├── historico.py
    └── interface.py
```

---

## ▶️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

### 2. Entre na pasta do projeto

```bash
cd ProjetoPyControleEstoque
```

### 3. Execute o sistema

```bash
python main.py
```

---

## 🔑 Login Padrão

Caso o arquivo `usuarios.json` utilize o usuário padrão:

```json
{
    "usuario": "admin",
    "senha": "123"
}
```

---

## 📸 Funcionalidades Implementadas

✅ Login de usuários

✅ Cadastro de produtos

✅ Edição de produtos

✅ Exclusão de produtos

✅ Entrada de estoque

✅ Saída de estoque

✅ Pesquisa de produtos

✅ Dashboard de indicadores

✅ Histórico de movimentações

✅ Controle de estoque mínimo

✅ Armazenamento em JSON

---

## 🎯 Melhorias Futuras

* Exportação para Excel
* Geração de relatórios PDF
* Gráficos estatísticos
* Interface moderna com ttkbootstrap
* Controle de permissões de usuários
* Backup automático dos dados

---

## 👨‍💻 Autor

Projeto desenvolvido para fins acadêmicos e aprendizado de desenvolvimento desktop com Python, Tkinter e manipulação de arquivos JSON.
