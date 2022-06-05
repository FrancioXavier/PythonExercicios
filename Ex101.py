from datetime import date


def voto(ano):
    idade = date.today().year - ano
    if idade < 18:
        return f'você tem {idade} anos e NÃO VOTA'
    if 65 > idade > 18:
        return f'Você tem {idade} anos e o voto é OBRIGATÓRIO'
    if idade > 65:
        return f'Você tem {idade} anos e o voto é OPCIONAL'


print('~='*20)
voto(int(input('Digite seu ano de nascimento: ')))
