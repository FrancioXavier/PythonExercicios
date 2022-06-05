import random
q = 0
escolhido = random.randint(0, 10)
n = int(input('Tente advinhar o numero sorteado por mim(: : '))
while n != escolhido:
    print('Errou, otário, tenta de novo')
    n = int(input('Advinhe aqui: '))
    q += 1
print('PARABÉNS! Você acertou! Precisou de {} tentativas.'.format(q))
