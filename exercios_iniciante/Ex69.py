c = ci = ch = cm = 0
while True:
    idade = int(input('Idade da pesssoa cadastrada: '))
    sexo = int(input('''sexo da pessoa cadastrada:
     [1] Masculino
     [2] Feminino
     [3] Outro
     Sua opção: '''))
    c += 1
    if idade > 18:
        ci += 1
    if sexo == 1:
        ch += 1
    if sexo == 2:
        if idade < 20:
            cm += 1
    p = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if p == 'N':
        break
    while p != 'S':
        p = str(input('Quer continuar? [S/N]')).upper().strip()[0]
print('Fim do processo.')
print(f'''Foram cadastrados {c} pessoas:
{ci} pessoas maiores que 18 anos
{ch} homens
{cm} mulheres menores que 20 anos''')


