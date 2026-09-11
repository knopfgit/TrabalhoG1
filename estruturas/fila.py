from estruturas.nodo import Nodo
from estruturas.erros import EstruturaVaziaError


class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    def enfileirar(self, valor):
        novo = Nodo(valor)
        if self.fim is None:
            self.inicio = self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo
        self.tamanho += 1

    def desenfileirar(self):
        if self.inicio is None:
            raise EstruturaVaziaError("A fila de vendas está vazia.")
        no = self.inicio
        self.inicio = no.proximo
        if self.inicio is None:
            self.fim = None
        self.tamanho -= 1
        return no.valor

    def frente(self):
        if self.inicio is None:
            raise EstruturaVaziaError("A fila de vendas está vazia.")
        return self.inicio.valor

    def remover_ultimo(self):
        if self.inicio is None:
            raise EstruturaVaziaError("A fila de vendas está vazia.")
        if self.inicio is self.fim:
            valor = self.inicio.valor
            self.inicio = self.fim = None
            self.tamanho -= 1
            return valor
        atual = self.inicio
        while atual.proximo is not self.fim:
            atual = atual.proximo
        valor = self.fim.valor
        atual.proximo = None
        self.fim = atual
        self.tamanho -= 1
        return valor

    def __iter__(self):
        atual = self.inicio
        while atual is not None:
            yield atual.valor
            atual = atual.proximo

    def __len__(self):
        return self.tamanho
