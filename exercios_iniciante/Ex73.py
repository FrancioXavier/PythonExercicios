times = ('Kabum!', 'FURIA', 'Red Canids', 'paiN', 'Netshoes', 'Liberty', 'Loud', 'Rensga', 'Flamengo', 'INTZ')
print('UPPER BRACKET: ')
print('='*20)
for pos, playoff in enumerate(times[:4]):
    print(f'{pos+1}o lugar: {playoff}')
print('='*20)
print('TIMES DESCLASSIFICADOS: ')
print('='*20)
for pos, fora in enumerate(times[6:]):
    print(f'{pos+7}o lugar: {fora}')
print('='*20)
print(f'Ordem alfabética: {sorted(times)}')
print('='*20)
for cont in range(0, len(times)):
    if cont == 4:
        print(f'O time paiN Gaming está na posição {cont}')
