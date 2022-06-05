dic = {}
dic['Nome'] = str(input('Digite o nome do aluno: '))
m = float(input('Digite a média do aluno: '))
dic['media'] = m
if m < 7:
    dic['situação'] = 'Reprovado'
else:
    dic['situação'] = 'Aprovado'
for k, v in dic.items():
    print(f'{k} = {v}')
