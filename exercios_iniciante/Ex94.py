pessoa = {}
dic = {}
lis = []
lism = []
lisi = []
som = mi = c = 0
while True:
    dic['nome'] = str(input('Digite o nome: '))
    i = int(input('Digite a idade: '))
    dic['idade'] = i
    som += i
    dic['sexo'] = str(input('Digite seu sexo: [M/F]'))
    pessoa[f'pessoa{c+1}'] = dic.copy()
    if pessoa[f'pessoa{c+1}']['sexo'][0] in 'Ff':
        lism.append(pessoa[f'pessoa{c + 1}'])
    dic.clear()
    c += 1
    p = str(input('Quer continuar? [S/N]'))
    if p in 'Nn':
        break
mi = som/c
for cont in range(0, len(pessoa)):
    if pessoa[f'pessoa{cont+1}']['idade'] > mi:
        lisi.append(pessoa[f'pessoa{cont+1}'])
print(f'foram cadastradas {c} pessoas')
print('*'*30)
print(f'a média de idade é {mi}')
print(f'as mulheres cadastradas foram: ')
for i, v in enumerate(lism):
    print(f'{v["nome"]}, {v["idade"]} anos')
print(f'As pessoas com idade acima da média: ')
for i, v in enumerate(lisi):
    print(f'{v["nome"]}, {v["idade"]} anos')
