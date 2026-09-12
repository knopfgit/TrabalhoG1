from algoritmos.busca_binaria import busca_binaria
from algoritmos.ordenacao import insertion_sort
from estruturas.erros import EstruturaVaziaError
from estruturas.fila import Fila
from estruturas.lde import LDE
from estruturas.lse import LSE
from estruturas.pilha import Pilha
from models.cliente import Cliente
from models.produto import Produto
from models.venda import ItemVenda, Venda
from services.estoque_service import (
    atualizar_estoque,
    valor_estoque,
    verificar_estoque
)
from services.persistencia_service import (
    carregar_tudo,
    salvar_tudo
)


class Sistema:
    def __init__(self):
        self.clientes = LSE()
        self.produtos = LDE()
        self.vendas = Fila()
        self.historico = Pilha()

        carregar_tudo(
            self.clientes,
            self.produtos,
            self.vendas
        )

        for venda in self.vendas:
            self.historico.empilhar(venda)

        self.proximo_id_venda = (
            self._calcular_proximo_id_venda()
        )

    def _calcular_proximo_id_venda(self):
        maior = 0

        for venda in self.vendas:
            if venda.id > maior:
                maior = venda.id

        return maior + 1

    def salvar(self):
        salvar_tudo(
            self.clientes,
            self.produtos,
            self.vendas
        )

    def _ler_inteiro(self, mensagem, minimo=None):
        valor = input(mensagem).strip()

        try:
            numero = int(valor)
        except ValueError:
            print(
                "Erro: informe um número inteiro válido."
            )
            return None

        if minimo is not None and numero < minimo:
            print(
                f"Erro: o valor deve ser maior ou igual a {minimo}."
            )
            return None

        return numero

    def _ler_decimal(self, mensagem):
        valor = (
            input(mensagem)
            .strip()
            .replace(",", ".")
        )

        try:
            numero = float(valor)
        except ValueError:
            print(
                "Erro: informe um preço numérico válido."
            )
            return None

        if numero <= 0:
            print(
                "Erro: o preço deve ser maior que zero."
            )
            return None

        return numero

    def cadastrar_cliente(self):
        cliente_id = self._ler_inteiro(
            "ID do cliente: ",
            1
        )

        if cliente_id is None:
            return

        if self.clientes.buscar(cliente_id) is not None:
            print(
                "Erro: já existe um cliente com esse ID."
            )
            return

        nome = input(
            "Nome do cliente: "
        ).strip()

        if not nome:
            print(
                "Erro: o nome é obrigatório."
            )
            return

        self.clientes.inserir(
            Cliente(cliente_id, nome)
        )

        self.salvar()

        print(
            "Cliente cadastrado com sucesso."
        )

    def listar_clientes(self):
        if self.clientes.esta_vazia():
            print(
                "Nenhum cliente cadastrado."
            )
            return

        print(
            "\n--- CLIENTES ---"
        )

        for cliente in self.clientes:
            print(cliente)

    def buscar_cliente(self):
        cliente_id = self._ler_inteiro(
            "ID do cliente: ",
            1
        )

        if cliente_id is None:
            return

        cliente = self.clientes.buscar(
            cliente_id
        )

        print(
            cliente
            if cliente
            else "Cliente não encontrado."
        )

    def remover_cliente(self):
        cliente_id = self._ler_inteiro(
            "ID do cliente: ",
            1
        )

        if cliente_id is None:
            return

        cliente = self.clientes.remover(
            cliente_id
        )

        if cliente is None:
            print(
                "Cliente não encontrado."
            )
            return

        self.salvar()

        print(
            "Cliente removido com sucesso."
        )

    def cadastrar_produto(self):
        produto_id = self._ler_inteiro(
            "ID do produto: ",
            1
        )

        if produto_id is None:
            return

        if self.produtos.buscar(produto_id) is not None:
            print(
                "Erro: já existe um produto com esse ID."
            )
            return

        nome = input(
            "Nome do produto: "
        ).strip()

        if not nome:
            print(
                "Erro: o nome é obrigatório."
            )
            return

        quantidade = self._ler_inteiro(
            "Quantidade inicial: ",
            0
        )

        if quantidade is None:
            return

        preco = self._ler_decimal(
            "Preço: R$ "
        )

        if preco is None:
            return

        self.produtos.inserir(
            Produto(
                produto_id,
                nome,
                quantidade,
                preco
            )
        )

        self.salvar()

        print(
            "Produto cadastrado com sucesso."
        )

    def listar_produtos(self):
        if self.produtos.esta_vazia():
            print(
                "Nenhum produto cadastrado."
            )
            return

        print(
            "\n--- PRODUTOS ---"
        )

        for produto in self.produtos:
            print(produto)

    def buscar_produto(self):
        produto_id = self._ler_inteiro(
            "ID do produto: ",
            1
        )

        if produto_id is None:
            return

        produto = self.produtos.buscar(
            produto_id
        )

        print(
            produto
            if produto
            else "Produto não encontrado."
        )

    def atualizar_estoque(self):
        produto_id = self._ler_inteiro(
            "ID do produto: ",
            1
        )

        if produto_id is None:
            return

        produto = self.produtos.buscar(
            produto_id
        )

        if produto is None:
            print(
                "Produto não encontrado."
            )
            return

        quantidade = self._ler_inteiro(
            "Alteração na quantidade (+entrada / -saída): "
        )

        if quantidade is None:
            return

        try:
            atualizar_estoque(
                produto,
                quantidade
            )
        except ValueError as erro:
            print(
                f"Erro: {erro}"
            )
            return

        self.salvar()

        print(
            "Estoque atualizado com sucesso."
        )

    def remover_produto(self):
        produto_id = self._ler_inteiro(
            "ID do produto: ",
            1
        )

        if produto_id is None:
            return

        produto = self.produtos.remover(
            produto_id
        )

        if produto is None:
            print(
                "Produto não encontrado."
            )
            return

        self.salvar()

        print(
            "Produto removido com sucesso."
        )

    def listar_produtos_inverso(self):
        if self.produtos.esta_vazia():
            print(
                "Nenhum produto cadastrado."
            )
            return

        print(
            "\n--- PRODUTOS (FIM -> INÍCIO) ---"
        )

        for produto in self.produtos.para_lista_fim_inicio():
            print(produto)

    def listar_produtos_ordenados(self):
        if self.produtos.esta_vazia():
            print(
                "Nenhum produto cadastrado."
            )
            return

        produtos_ordenados = insertion_sort(
            self.produtos.para_lista_inicio_fim()
        )

        print(
            "\n--- PRODUTOS ORDENADOS POR ID (INSERTION SORT) ---"
        )

        for produto in produtos_ordenados:
            print(produto)

    def buscar_produto_binario(self):
        produto_id = self._ler_inteiro(
            "ID do produto: ",
            1
        )

        if produto_id is None:
            return

        produtos_ordenados = insertion_sort(
            self.produtos.para_lista_inicio_fim()
        )

        produto = busca_binaria(
            produtos_ordenados,
            produto_id
        )

        print(
            produto
            if produto
            else "Produto não encontrado."
        )

    def realizar_venda(self):
        if self.clientes.esta_vazia():
            print(
                "Erro: cadastre pelo menos um cliente "
                "antes de realizar uma venda."
            )
            return

        if self.produtos.esta_vazia():
            print(
                "Erro: cadastre pelo menos um produto "
                "antes de realizar uma venda."
            )
            return

        cliente_id = self._ler_inteiro(
            "ID do cliente: ",
            1
        )

        if cliente_id is None:
            return

        cliente = self.clientes.buscar(
            cliente_id
        )

        if cliente is None:
            print(
                "Erro: cliente não encontrado. "
                "Venda cancelada."
            )
            return

        itens = []
        ids_inseridos = set()

        print(
            "Digite 0 no ID do produto para finalizar a venda."
        )

        while True:
            produto_id = self._ler_inteiro(
                "ID do produto: ",
                0
            )

            if produto_id is None:
                return

            if produto_id == 0:
                break

            if produto_id in ids_inseridos:
                print(
                    "Erro: esse produto já foi informado "
                    "nesta venda."
                )
                return

            produto = self.produtos.buscar(
                produto_id
            )

            if produto is None:
                print(
                    "Erro: produto não encontrado. "
                    "Venda cancelada."
                )
                return

            quantidade = self._ler_inteiro(
                "Quantidade: ",
                1
            )

            if quantidade is None:
                return

            if not verificar_estoque(
                produto,
                quantidade
            ):
                print(
                    f"Erro: estoque insuficiente para "
                    f"'{produto.nome}'. Venda cancelada."
                )
                return

            itens.append(
                ItemVenda(
                    produto.id,
                    produto.nome,
                    quantidade,
                    produto.preco
                )
            )

            ids_inseridos.add(
                produto.id
            )

            print(
                f"Item adicionado: "
                f"{produto.nome} x{quantidade}."
            )

        if not itens:
            print(
                "Erro: a venda deve conter pelo menos "
                "um produto."
            )
            return

        venda = Venda(
            self.proximo_id_venda,
            cliente.id,
            cliente.nome,
            itens
        )

        for item in itens:
            produto = self.produtos.buscar(
                item.produto_id
            )

            atualizar_estoque(
                produto,
                -item.quantidade
            )

        self.vendas.enfileirar(
            venda
        )

        self.historico.empilhar(
            venda
        )

        self.proximo_id_venda += 1

        self.salvar()

        print(
            "\nVenda realizada com sucesso!"
        )

        print(venda)

    def visualizar_fila(self):
        if self.vendas.esta_vazia():
            print(
                "A fila de vendas está vazia."
            )
            return

        print(
            "\n--- FILA DE VENDAS (FIFO) ---"
        )

        for venda in self.vendas:
            print(venda)

    def visualizar_primeira_venda(self):
        try:
            venda = self.vendas.frente()
            print(venda)

        except EstruturaVaziaError as erro:
            print(erro)

    def total_estoque(self):
        print(
            f"Valor total do estoque: "
            f"R$ {valor_estoque(self.produtos):.2f}"
        )

    def total_vendas(self):
        total = 0

        for venda in self.vendas:
            total += venda.valor_total

        print(
            f"Valor total das vendas: "
            f"R$ {total:.2f}"
        )

    def clientes_valores(self):
        if self.clientes.esta_vazia():
            print(
                "Nenhum cliente cadastrado."
            )
            return

        totais = {}

        for cliente in self.clientes:
            totais[cliente.id] = 0

        for venda in self.vendas:
            totais[venda.cliente_id] = (
                totais.get(
                    venda.cliente_id,
                    0
                )
                + venda.valor_total
            )

        print(
            "\n--- TOTAL GASTO POR CLIENTE ---"
        )

        for cliente in self.clientes:
            print(
                f"{cliente.nome} "
                f"(ID {cliente.id}): "
                f"R$ {totais[cliente.id]:.2f}"
            )

    def cliente_que_mais_gastou(self):
        if self.clientes.esta_vazia():
            print(
                "Nenhum cliente cadastrado."
            )
            return

        melhor = None
        maior = -1

        for cliente in self.clientes:
            total = 0

            for venda in self.vendas:
                if venda.cliente_id == cliente.id:
                    total += venda.valor_total

            if total > maior:
                maior = total
                melhor = cliente

        print(
            f"Cliente que mais gastou: "
            f"{melhor.nome} "
            f"(ID {melhor.id}) - "
            f"R$ {maior:.2f}"
        )

    def produto_mais_vendido(self):
        if self.produtos.esta_vazia():
            print(
                "Nenhum produto cadastrado."
            )
            return

        quantidades = {}
        nomes = {}

        for venda in self.vendas:
            for item in venda.itens:
                quantidades[item.produto_id] = (
                    quantidades.get(
                        item.produto_id,
                        0
                    )
                    + item.quantidade
                )

                nomes[item.produto_id] = (
                    item.nome
                )

        if not quantidades:
            print(
                "Ainda não existem vendas registradas."
            )
            return

        melhor_id = None
        maior = -1

        for produto_id, quantidade in quantidades.items():
            if quantidade > maior:
                maior = quantidade
                melhor_id = produto_id

        print(
            f"Produto mais vendido: "
            f"{nomes[melhor_id]} "
            f"(ID {melhor_id}) - "
            f"{maior} unidade(s)"
        )

    def desfazer(self):
        try:
            venda = self.historico.desempilhar()

        except EstruturaVaziaError as erro:
            print(erro)
            return

        try:
            ultima = self.vendas.remover_ultimo()

        except EstruturaVaziaError:
            print(
                "Erro: não foi possível desfazer a operação "
                "porque a fila está vazia."
            )

            self.historico.empilhar(
                venda
            )

            return

        if ultima.id != venda.id:
            print(
                "Erro: histórico inconsistente. "
                "Operação não desfeita."
            )

            self.historico.empilhar(
                venda
            )

            self.vendas.enfileirar(
                ultima
            )

            return

        for item in venda.itens:
            produto = self.produtos.buscar(
                item.produto_id
            )

            if produto is not None:
                atualizar_estoque(
                    produto,
                    item.quantidade
                )

        self.proximo_id_venda = max(
            1,
            venda.id
        )

        self.salvar()

        print(
            f"Venda #{venda.id} desfeita com sucesso. "
            "Estoque restaurado."
        )

    def menu(self):
        while True:
            print("""
==============================
 SISTEMA DE ESTOQUE E VENDAS
==============================
1 - Cadastrar cliente
2 - Listar clientes
3 - Buscar cliente
4 - Remover cliente
5 - Cadastrar produto
6 - Listar produtos
7 - Buscar produto
8 - Atualizar estoque
9 - Remover produto
10 - Listar produtos em ordem inversa
11 - Listar produtos ordenados
12 - Buscar produto por ID usando Busca Binária
13 - Realizar venda
14 - Visualizar fila de vendas
15 - Visualizar primeira venda da fila
16 - Exibir valor total do estoque
17 - Exibir valor total das vendas
18 - Exibir clientes e valores totais gastos
19 - Exibir cliente que mais gastou
20 - Exibir produto mais vendido
21 - Desfazer última operação
0 - Sair
""")

            opcao = input(
                "Escolha uma opção: "
            ).strip()

            acoes = {
                "1": self.cadastrar_cliente,
                "2": self.listar_clientes,
                "3": self.buscar_cliente,
                "4": self.remover_cliente,
                "5": self.cadastrar_produto,
                "6": self.listar_produtos,
                "7": self.buscar_produto,
                "8": self.atualizar_estoque,
                "9": self.remover_produto,
                "10": self.listar_produtos_inverso,
                "11": self.listar_produtos_ordenados,
                "12": self.buscar_produto_binario,
                "13": self.realizar_venda,
                "14": self.visualizar_fila,
                "15": self.visualizar_primeira_venda,
                "16": self.total_estoque,
                "17": self.total_vendas,
                "18": self.clientes_valores,
                "19": self.cliente_que_mais_gastou,
                "20": self.produto_mais_vendido,
                "21": self.desfazer,
            }

            if opcao == "0":
                self.salvar()

                print(
                    "Programa encerrado."
                )

                break

            acao = acoes.get(
                opcao
            )

            if acao is None:
                print(
                    "Opção inválida. "
                    "Escolha uma opção do menu."
                )
                continue

            try:
                acao()

            except (
                EOFError,
                KeyboardInterrupt
            ):
                print(
                    "\nEntrada interrompida. "
                    "Voltando ao menu."
                )

            except Exception as erro:
                print(
                    f"Erro inesperado tratado: {erro}"
                )


if __name__ == "__main__":
    Sistema().menu()