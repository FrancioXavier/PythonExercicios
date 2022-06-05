c50 = c20 = c10 = c1 = r2 = r = 0
while True:
    sac = int(input('Digite quanto você quer sacar: '))
    if sac >= 50:
        c50 = sac // 50
        r = sac % 50
    if r >= 20:
        c20 = r // 20
        r = r % 20
    if r >= 10:
        c10 = r // 10
        r = r % 10
    if r >= 1:
        c1 = r
        r2 = r % 1
        break
print(f'''Você vai receber: 
{c50} cédulas de 50 reais 
{c20} cédulas de 20 reais 
{c10} cédulas de 10 reais 
{c1} cédulas de 1 real''')
