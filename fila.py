class Fila:
    def __init__(self):
        self.fila = []

    def inserir(self, n):
        self.fila.append(n)

    def excluir(self):
        if not self.vazia():
            return self.fila.pop(0)

    def tamanho(self):
        return len(self.fila)

    def vazia(self):
        return self.tamanho == 0


f1 = Fila()
f1.inserir(1)
f1.inserir(2)
print(f1.excluir())
print(f1.tamanho())

