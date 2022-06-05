print('='*15)
print(f'TABUADA')
print('='*15)
while True:
    n = int(input('''Digite um número para ver a tabuada (para 
parar o programa digite um número negativo): '''))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')
print('Programa desativado')
