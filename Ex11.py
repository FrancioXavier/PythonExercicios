alt = float(input('Digite a altura da parede: '))
lar = float(input('Digite a largura da parede: '))
a = alt*lar
quant = a/2
print('A área da parede é {:.3f} metros quadradados e será necessário {:.3f} litros de tinta'.format(a, quant))
