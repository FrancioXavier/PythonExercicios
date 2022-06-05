listagem = ('Frango', 10,
            'Bisteca', 15,
            'Ovo', 8.50,
            'Arroz', 5,
            'Feijão', 4)
print('~='*20)
print('Listagem de preços')
print('~='*20)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:.2f}')
