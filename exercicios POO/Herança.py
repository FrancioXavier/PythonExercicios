class NPC:
    def __init__(self, nome, time, forca, municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100

    def info(self):
        print(f'''nome...:{self.nome:}
time...:{self.time}
força..:{self.forca:}
munição:{self.municao}''')


class Soldado(NPC):
    def __init__(self, nome, time, forca, municao):
        super().__init__(nome, time, forca, municao)

    def inf(self):
        super().info()


s1 = Soldado('Geraldo', 2, 30, 50)
s1.inf()

