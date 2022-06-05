tupla = ('palavra', 'muita', 'robrok', 'eita', 'coisa', 'pereba')
for p in tupla:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra.upper(), end=' ')
