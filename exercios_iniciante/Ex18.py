import math
a = float(input('Digite um angulo qualquer: '))

print(' Cosseno do angulo {} é: {:.3f} \n O seno: {:.3f} \n E a tangente: {:.3f}'.format(a, math.cos(math.radians(a)), math.sin(math.radians(a)), math.tan(math.radians(a))))
