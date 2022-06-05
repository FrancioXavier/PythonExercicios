class Carrinho:
    def __init__(self):
        self.produto = []

    def inserir_produto(self, produto):
        self.produto.append(produto)

    def ListaProduto(self):
        for produto in self.produto:
            print(f'O produto {produto.nome} é {produto.valor} reais')

    def Soma(self):
        som = 0
        for produto in self.produto:
            som += produto.valor
        return som


class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor


p1 = Produto('Feijão', 5)
p2 = Produto('Arroz', 4)
c1 = Carrinho()
c1.inserir_produto(p1)
c1.inserir_produto(p2)
c1.ListaProduto()
print(f'a soma da compra é {c1.Soma()} reais')
