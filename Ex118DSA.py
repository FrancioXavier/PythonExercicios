class Celular:
    def __init__(self, tamanho, interface):
        self.tamanho = tamanho
        self.interface = interface


class Mp3(Celular):
    def __init__(self, capacidade, tamanho=12, interface='android'):
        Celular.__init__(self, tamanho, interface)
        self.capacidade = capacidade

    def print_Mp3(self):
        print(f'A capacidade do mp3 é {self.capacidade}, tem tamanho {self.tamanho} e interface {self.interface}')


A20 = Mp3('32gb', 15)
A20.print_Mp3()
