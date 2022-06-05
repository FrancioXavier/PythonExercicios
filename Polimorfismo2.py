class Animal:
    def __init__(self, nome):
        self.nome = nome

    def Emitir_som(self):
        pass


class Humano(Animal):
    def __init__(self, nome):
        super(Humano, self).__init__(nome)

    def Emitir_som(self):
        return print(f'Olá, {self.nome}')


class Peixe(Animal):
    def __init__(self, nome):
        super(Peixe, self).__init__(nome)

    def Emitir_som(self):
        return print(f'Eu sou {self.nome}')


p1 = Peixe('Clara Lírio')
p1.Emitir_som()