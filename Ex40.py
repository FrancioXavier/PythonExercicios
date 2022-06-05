cores = {'vermelho': '\033[31m',
         'azul': '\033[34m',
         'limpa': '\033[m',
         'branco': '\033[30m'}
print('=' * 21)
print('{}       BOLETIM{}'.format(cores['azul'], cores['limpa']))
print('=' * 21)
n = str(input('Digite o nome do aluno: ')).strip()
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
m = (n1 + n2)/2
if m < 5:
    print('''O aluno {} tem média {}{:.1f}{}. 
Resultado final: reprovado'''.format(n, cores['vermelho'], m, cores['limpa']))
elif 5 < m < 6.9:
    print('''O aluno {} tem média {}{:.1f}{}. 
Resultado final: recuperação'''.format(n, cores['branco'], m, cores['limpa']))
else:
    print('''O aluno {} tem média {}{:.1f}{}. 
Resultado final: aprovado! Parabéns!'''.format(n, cores['azul'], m, cores['limpa']))


