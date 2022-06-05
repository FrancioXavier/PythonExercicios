jogador = {}
time = list()
g = list()
s = 0
while True:
    jogador.clear()
    jogador['nome'] = str(input('Digite o nome do jogador: '))
    p = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    for c in range(0, p):
        g.append(int(input(f'Quantidade de gols na partida {c+1}: ')))
    jogador['Gols'] = g[:]
    jogador['total'] = sum(g)
    time.append(jogador.copy())
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print(time)
print('=='*30)
print(f'{"TIME":^30}')
print('=='*30)
print('Cód. ', end='')
for k in jogador.keys():
    print(f'{k:<15}', end='')
print()
print('=='*30)
for i, v in enumerate(time):
    print(f'{i:>3}', end='  ')
    for p in v.values():
        print(f'{str(p):<15}', end=' ')
    print()
while True:
    esc = int(input('Digite o código do jogador que queira saber os aproveitamentos (999 para): '))
    if esc == 999:
        break
    if esc > len(time):
        print('ERRO! Digite um código válido.')
    else:
        print(f'APROVEITAMENTO DO JOGADOR {time[esc]["nome"]}')
        for i, g in enumerate(time[esc]["Gols"]):
            print(f'Jogo {i+1}: {g} gols')
