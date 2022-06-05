from random import randint


class Tamaguchi:

    def __init__(self, nome, saude, idade, fome=2, tedio=5):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade
        self.tedio = tedio
        self.tamaguchi = [self.nome, self.fome, self.saude, self.idade, self.tedio]

    def Alterar_nome(self, novo):
        self.nome = novo
        return print(f'Novo nome {self.nome}')

    def Alterar_fome(self, novo):
        self.fome = novo
        return print(f'Novo índice de fome {self.fome}')

    def Alterar_saude(self, novo):
        self.saude = novo
        return print(f'Novo indice de saúde {self.saude}')

    def Alterar_idade(self, novo):
        self.idade = novo
        return print(f'Nova idade é {self.idade}')

    def humor(self):
        humor = (self.fome + self.saude)/2
        if humor < 5:
            return print(f'O {self.nome} tá PUUUUUUUUUUTO')
        elif 5 < humor < 7:
            return print(f'O {self.nome} tá normal')
        else:
            return print(f'O {self.nome} tá feliz')

    def Dar_comida(self, quant):
        if quant > self.fome:
            return print(f'Muita comida! reduza quantidade para {self.fome} de comida')
        elif quant == self.fome:
            self.fome = 0
            return print(f'O Tamaguchi está satisfeito!')
        else:
            Nfome = self.fome - quant
            return print(f'O tamaguchi ainda precisa de {Nfome} de comida')

    def Brincar(self, brinca):
        if brinca > self.tedio:
            return print(f'Muita comida! reduza quantidade para {self.tedio} de comida')
        elif brinca == self.tedio:
            return print(f'O Tamaguchi está satisfeito!')
        else:
            Ntedio = self.tedio - brinca
            return print(f'O tamaguchi ainda precisa brincar {Ntedio} vezes')

    def Dados(self):
        return print(f'''
                Nome.: {self.nome}
                Fome.: {self.fome}
                Saúde: {self.saude}
                idade: {self.idade} anos
                Tédio: {self.tedio}
                ''')


class Fazenda:

    def __init__(self):
        self.fazenda = []

    def adiciona(self, obj):
        self.fazenda.append(obj)

    def mostrar_fazenda(self):
        pass


t1 = Tamaguchi('Jonas', 10, 3)
fazenda = Fazenda()
fazenda.adiciona(t1.tamaguchi)
print(fazenda.fazenda)







