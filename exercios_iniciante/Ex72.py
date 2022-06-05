ne = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
ler = int(input('Digite um numero de zero a vinte: '))
if ler < 0 or ler > 20:
    ler = int(input('Tente novamente, digite um numero entre 0 e 20: '))
print(f'O número por extenso é {ne[ler]}')
