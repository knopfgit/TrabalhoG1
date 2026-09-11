from estruturas.nodo import NodoDuplo


class LDE:
    def __init__(self):
        self.cabeca = None
        self.cauda = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.cabeca is None

    def inserir(self, produto):
        novo = NodoDuplo(produto)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo
        else:
            novo.anterior = self.cauda
            self.cauda.proximo = novo
            self.cauda = novo
        self.tamanho += 1

    def buscar(self, produto_id):
        atual = self.cabeca
        while atual is not None:
            if atual.valor.id == produto_id:
                return atual.valor
            atual = atual.proximo
        return None

    def remover(self, produto_id):
        atual = self.cabeca
        while atual is not None:
            if atual.valor.id == produto_id:
                if atual.anterior is not None:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.cabeca = atual.proximo
                if atual.proximo is not None:
                    atual.proximo.anterior = atual.anterior
                else:
                    self.cauda = atual.anterior
                self.tamanho -= 1
                return atual.valor
            atual = atual.proximo
        return None

    def para_lista_inicio_fim(self):
        resultado = []
        atual = self.cabeca
        while atual is not None:
            resultado.append(atual.valor)
            atual = atual.proximo
        return resultado

    def para_lista_fim_inicio(self):
        resultado = []
        atual = self.cauda
        while atual is not None:
            resultado.append(atual.valor)
            atual = atual.anterior
        return resultado

    def __iter__(self):
        atual = self.cabeca
        while atual is not None:
            yield atual.valor
            atual = atual.proximo

    def __len__(self):
        return self.tamanho
