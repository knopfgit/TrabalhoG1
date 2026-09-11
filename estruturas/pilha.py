from estruturas.nodo import Nodo
from estruturas.erros import EstruturaVaziaError


class Pilha:
    def __init__(self):
        self.topo_no = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.topo_no is None

    def empilhar(self, valor):
        novo = Nodo(valor)
        novo.proximo = self.topo_no
        self.topo_no = novo
        self.tamanho += 1

    def desempilhar(self):
        if self.topo_no is None:
            raise EstruturaVaziaError("Não há operações para desfazer.")
        no = self.topo_no
        self.topo_no = no.proximo
        self.tamanho -= 1
        return no.valor

    def topo(self):
        if self.topo_no is None:
            raise EstruturaVaziaError("A pilha está vazia.")
        return self.topo_no.valor

    def __iter__(self):
        atual = self.topo_no
        while atual is not None:
            yield atual.valor
            atual = atual.proximo

    def __len__(self):
        return self.tamanho
