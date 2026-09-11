from estruturas.nodo import Nodo


class LSE:
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.cabeca is None

    def inserir(self, cliente):
        novo = Nodo(cliente)
        if self.cabeca is None:
            self.cabeca = novo
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo
        self.tamanho += 1

    def buscar(self, cliente_id):
        atual = self.cabeca
        while atual is not None:
            if atual.valor.id == cliente_id:
                return atual.valor
            atual = atual.proximo
        return None

    def remover(self, cliente_id):
        atual = self.cabeca
        anterior = None
        while atual is not None:
            if atual.valor.id == cliente_id:
                if anterior is None:
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self.tamanho -= 1
                return atual.valor
            anterior = atual
            atual = atual.proximo
        return None

    def __iter__(self):
        atual = self.cabeca
        while atual is not None:
            yield atual.valor
            atual = atual.proximo

    def __len__(self):
        return self.tamanho
