def area(a, b):
    area = a * b
    print(f'A área do terreno é {area:.2f}m²')


print('~='*20)
print(f'{"CONTROLE DE TERRENOS":^40}')
print('~='*20)
area(a=float(input('Digite a largura(m): ')), b=float(input('Digite o comprimento(m): ')))
