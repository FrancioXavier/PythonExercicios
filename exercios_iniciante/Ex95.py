if k == 'nome':
    print(f'O jogador {v}', end=' ')
if k == 'partidas':
    print(f'jogou {v} {k}')
if k == 'gol por partida':
    for c in range(0, q):
        print(f'-> na partida {c + 1} ele fez {v[c]} gols')
if k == 'total de gols':
    print(f'{k} = {v}')