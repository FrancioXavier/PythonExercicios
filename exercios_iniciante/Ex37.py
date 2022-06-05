n = int(input('Digite um numero qualquer: '))
print('''Escolha o tipo de conversão: 
[1] Para BINÁRIO
[2] Para OCTAL
[3] Para HEXADECIMAL''')
op = int(input('Sua opção: '))
if op == 1:
    print('O número {} foi convertido para binário: {}'.format(n, bin(n)[2:]))
elif op == 2:
    print('O número {} foi convertido para octal: {}'.format(n, oct(n)[2:]))
elif op == 3:
    print('O número {} foi convertido para hexadecimal: {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida')
