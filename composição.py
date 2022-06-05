class Cliente:
    def __init__(self, nome, idade):
        self.idade = idade
        self.nome = nome
        self.enderecos = []

    def Insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_endereco(self):
        for endereco in self.enderecos:
            print(f'Cidade: {endereco.cidade}/ estado: {endereco.estado}')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado


cliente1 = Cliente('Francio Xavier', 18)
cliente1.Insere_endereco('Juacity', 'Ceará')
cliente1.lista_endereco()
