import csv
import os

from models.cliente import Cliente
from models.produto import Produto


PASTA_DATA = "data"
ARQUIVO_CLIENTES = os.path.join(PASTA_DATA, "clientes.csv")
ARQUIVO_PRODUTOS = os.path.join(PASTA_DATA, "produtos.csv")
ARQUIVO_VENDAS = os.path.join(PASTA_DATA, "vendas.csv")


def preparar_pasta():
    os.makedirs(PASTA_DATA, exist_ok=True)


def salvar_clientes(lse):
    preparar_pasta()

    with open(ARQUIVO_CLIENTES, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["id", "nome"])

        atual = lse.inicio

        while atual is not None:
            escritor.writerow([atual.valor.id, atual.valor.nome])
            atual = atual.proximo


def carregar_clientes(lse):
    if not os.path.exists(ARQUIVO_CLIENTES):
        return

    with open(ARQUIVO_CLIENTES, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            cliente = Cliente(int(linha["id"]), linha["nome"])
            lse.inserir_fim(cliente)


def salvar_produtos(lde):
    preparar_pasta()

    with open(ARQUIVO_PRODUTOS, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["id", "nome", "quantidade", "preco"])

        atual = lde.inicio

        while atual is not None:
            produto = atual.valor
            escritor.writerow([
                produto.id,
                produto.nome,
                produto.quantidade,
                produto.preco
            ])
            atual = atual.proximo


def carregar_produtos(lde):
    if not os.path.exists(ARQUIVO_PRODUTOS):
        return

    with open(ARQUIVO_PRODUTOS, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            produto = Produto(
                int(linha["id"]),
                linha["nome"],
                int(linha["quantidade"]),
                float(linha["preco"])
            )
            lde.inserir_fim(produto)