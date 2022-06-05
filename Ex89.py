bo = []
while True:
    nome = str(input('Digite o nome: '))
    n1 = float(input('Digite a nota 1: '))
    n2 = float(input('Digite a nota 2: '))
    m = (n1 + n2)/2
    bo.append([nome, [n1, n2], m])
    p = str(input('Quer continuar? [S/N] '))
    if p in 'Nn':
        break
print('~='*20)
print('BOLETIM')
print('~='*20)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('--'*20)
for v, c in enumerate(bo):
    print(f'{v:<4}{c[0]:<10}{c[2]:>8.1f}')
print('--'*20)
while True:
    i = int(input('Digite o número do aluno que queira saber as notas (999 para parar): '))
    print(f'Nota 1 e 2 de {bo[i][0]}: {bo[i][1]}')
    if i == 999:
        break
