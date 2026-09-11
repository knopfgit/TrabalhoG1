class ItemVenda:
    def __init__(self, produto_id, nome, quantidade, preco_unitario):
        self.produto_id = produto_id
        self.nome = nome
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    @property
    def subtotal(self):
        return self.quantidade * self.preco_unitario


class Venda:
    def __init__(self, id, cliente_id, cliente_nome, itens):
        self.id = id
        self.cliente_id = cliente_id
        self.cliente_nome = cliente_nome
        self.itens = itens

    @property
    def valor_total(self):
        return sum(item.subtotal for item in self.itens)

    def __str__(self):
        linhas = [f"Venda #{self.id} - Cliente: {self.cliente_nome} "
                  f"(ID {self.cliente_id})"]
        for item in self.itens:
            linhas.append(
                f"    - {item.nome} x{item.quantidade} @ "
                f"R$ {item.preco_unitario:.2f} = R$ {item.subtotal:.2f}")
        linhas.append(f"    TOTAL: R$ {self.valor_total:.2f}")
        return "\n".join(linhas)
