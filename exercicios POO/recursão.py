def fatorial(n):
    if n == 1:#caso base: onde a função para pra n ficar num loop infinito
        return 1

    return n * fatorial(n-1)#caso recursivo: chama a propria função


print(fatorial(5))

#leis da recursividade
#1: toda função recursiva deve ter um caso base
#2: toda função recursiva deve chamar a ela msm(caso recursivo)
#3: a cada caso recursivo utilizado, deve se aproximar do caso base

