class Pessoa():

    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        self.amigos = []

    def __str__(self):
        return f'Seu nome é {self.nome} e tem {self.idade} anos \nEmail: {self.email} \nTel.: {self.telefone}'

    def mostrar_amigos(self):
        for i, v in enumerate(self.amigos[0]):
            str(print(f'amigo {str(i+1)}: {str(v)}'))



p1 = Pessoa('Francio', 18, 'francioxavier', 9147)
p1.amigos.append(['Vinicius', 'Almir', 'Tijolo', 'Igor'])
p1.mostrar_amigos()
