import csv
import os

from models.cliente import Cliente
from models.produto import Produto
from models.venda import ItemVenda, Venda


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

PASTA_DATA = os.path.join(
    BASE_DIR,
    "data"
)

ARQUIVO_CLIENTES = os.path.join(
    PASTA_DATA,
    "clientes.csv"
)

ARQUIVO_PRODUTOS = os.path.join(
    PASTA_DATA,
    "produtos.csv"
)

ARQUIVO_VENDAS = os.path.join(
    PASTA_DATA,
    "vendas.csv"
)


def preparar_pasta():
    os.makedirs(
        PASTA_DATA,
        exist_ok=True
    )


def salvar_clientes(lse):
    preparar_pasta()

    with open(
        ARQUIVO_CLIENTES,
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerow([
            "id",
            "nome"
        ])

        for cliente in lse:
            escritor.writerow([
                cliente.id,
                cliente.nome
            ])


def carregar_clientes(lse):
    if (
        not os.path.exists(ARQUIVO_CLIENTES)
        or os.path.getsize(ARQUIVO_CLIENTES) == 0
    ):
        return

    with open(
        ARQUIVO_CLIENTES,
        "r",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            try:
                lse.inserir(
                    Cliente(
                        int(linha["id"]),
                        linha["nome"]
                    )
                )

            except (
                KeyError,
                TypeError,
                ValueError
            ):
                continue


def salvar_produtos(lde):
    preparar_pasta()

    with open(
        ARQUIVO_PRODUTOS,
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerow([
            "id",
            "nome",
            "quantidade",
            "preco"
        ])

        for produto in lde:
            escritor.writerow([
                produto.id,
                produto.nome,
                produto.quantidade,
                produto.preco
            ])


def carregar_produtos(lde):
    if (
        not os.path.exists(ARQUIVO_PRODUTOS)
        or os.path.getsize(ARQUIVO_PRODUTOS) == 0
    ):
        return

    with open(
        ARQUIVO_PRODUTOS,
        "r",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            try:
                produto = Produto(
                    int(linha["id"]),
                    linha["nome"],
                    int(linha["quantidade"]),
                    float(linha["preco"])
                )

                if (
                    produto.id >= 0
                    and produto.quantidade >= 0
                    and produto.preco > 0
                ):
                    lde.inserir(produto)

            except (
                KeyError,
                TypeError,
                ValueError
            ):
                continue


def salvar_vendas(fila):
    preparar_pasta()

    with open(
        ARQUIVO_VENDAS,
        "w",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerow([
            "id_venda",
            "cliente_id",
            "cliente_nome",
            "produto_id",
            "produto_nome",
            "quantidade",
            "preco_unitario"
        ])

        for venda in fila:

            for item in venda.itens:
                escritor.writerow([
                    venda.id,
                    venda.cliente_id,
                    venda.cliente_nome,
                    item.produto_id,
                    item.nome,
                    item.quantidade,
                    item.preco_unitario
                ])


def carregar_vendas(fila):
    if (
        not os.path.exists(ARQUIVO_VENDAS)
        or os.path.getsize(ARQUIVO_VENDAS) == 0
    ):
        return

    vendas = []
    por_id = {}

    with open(
        ARQUIVO_VENDAS,
        "r",
        newline="",
        encoding="utf-8"
    ) as arquivo:

        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            try:
                id_venda = int(
                    linha["id_venda"]
                )

                cliente_id = int(
                    linha["cliente_id"]
                )

                item = ItemVenda(
                    int(linha["produto_id"]),
                    linha["produto_nome"],
                    int(linha["quantidade"]),
                    float(linha["preco_unitario"])
                )

                if id_venda not in por_id:

                    venda = Venda(
                        id_venda,
                        cliente_id,
                        linha["cliente_nome"],
                        []
                    )

                    por_id[id_venda] = venda
                    vendas.append(venda)

                por_id[id_venda].itens.append(
                    item
                )

            except (
                KeyError,
                TypeError,
                ValueError
            ):
                continue

    for venda in vendas:
        fila.enfileirar(venda)


def salvar_tudo(lse, lde, fila):
    salvar_clientes(lse)
    salvar_produtos(lde)
    salvar_vendas(fila)


def carregar_tudo(lse, lde, fila):
    preparar_pasta()

    carregar_clientes(lse)
    carregar_produtos(lde)
    carregar_vendas(fila)