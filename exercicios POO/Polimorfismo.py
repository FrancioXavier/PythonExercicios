class FiguraGeometrica:
    def __init__(self, lado):
        self.lado = lado

    def Calcula_area(self):
        pass


class Quadrado(FiguraGeometrica):
    def __init__(self, lado):
        super(Quadrado, self).__init__(lado)

    def Calcula_area(self):
        return print(f'{self.lado}²= {self.lado * self.lado}')


class Triangulo(FiguraGeometrica):
    def __init__(self, lado, altura):
        self.altura = altura
        super(Triangulo, self).__init__(lado)

    def Calcula_area(self):
        return print(f'O lado {self.lado} vezes a altura {self.altura} dividido por 2 é: {(self.lado*self.altura)/2}')


class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio
        super(Circulo, self).__init__(self)

    def Calcula_area(self):
        return print(f'A área do círculo é: {3.14*(self.raio*self.raio)}')




