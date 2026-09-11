class Produto:
    def __init__(self, id, nome, quantidade, preco):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return (f"Produto[ID={self.id}] {self.nome} | "
                f"estoque: {self.quantidade} | preço: R$ {self.preco:.2f}")
