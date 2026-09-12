def atualizar_estoque(produto, quantidade):
    nova_quantidade = produto.quantidade + quantidade

    if nova_quantidade < 0:
        raise ValueError("Estoque não pode ficar negativo.")

    produto.quantidade = nova_quantidade


def verificar_estoque(produto, quantidade):
    return produto.quantidade >= quantidade


def valor_estoque(produtos):
    total = 0

    for produto in produtos:
        total += produto.preco * produto.quantidade

    return total