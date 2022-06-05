f = str(input('Digite uma frase qualquer: ')).upper()
p = f.split()
junto = ''.join(p)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('A frase junta é {} e o inverso é {}'.format(junto, inverso))
if inverso == junto:
    print('A frase é um palíndromo!')
else:
    print('Não é palindromo')

