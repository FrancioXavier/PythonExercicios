import random
from time import sleep
lista = ['pedra', 'papel', 'tesoura']
bot = random.choice(lista)
player = str(input('Vamos jogar jokenpô! escolha pedra, papel ou tesoura: ')).lower().strip()
print('JO!')
sleep(0.5)
print('KEN!')
sleep(0.5)
print('PO!')
print('-='*20)
if player == 'pedra' and bot == 'tesoura':
    print('Eu escolhi {}, você escolheu {} \nVocê venceu;-;'.format(bot, player))
elif player == 'tesoura' and bot == 'papel':
    print('Eu escolhi {}, você escolheu {} \nVocê venceu;-;'.format(bot, player))
elif player == 'papel' and bot == 'pedra':
    print('Eu escolhi {}, você escolheu {} \nVocê venceu;-;'.format(bot, player))
elif bot == 'pedra' and player == 'tesoura':
    print('Eu escolhi {}, você escolheu {} \nEu venciii!!!'.format(bot, player))
elif bot == 'tesoura' and player == 'papel':
    print('Eu escolhi {}, você escolheu {} \nEu venciii!!!'.format(bot, player))
elif bot == 'papel' and player == 'pedra':
    print('Eu escolhi {}, você escolheu {} \nEu venciii!!!'.format(bot, player))
else:
    print('Empatamo')
print('-='*20)
