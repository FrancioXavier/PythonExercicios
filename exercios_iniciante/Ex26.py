frase = str(input('Digite uma frase qualquer: ')).upper().strip()
print('A letra "A" foi encontrada {} vezes: '.format(frase.count('A')))
print('A letra "A" foi encontrada a primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra "A" foi encontrada na ultima vez na posição {}'.format(frase.rfind('A')+1))

