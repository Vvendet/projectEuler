
import sys
numeros = []
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    numeros.append(n)
for a in numeros:
    soma = 0
    lista = list(range(0,a,3))
    for i in lista:
        if i%3==0 and i%5==0:
            pass
        elif i%3==0 and i%5!=0:
            soma += i
    lista = list(range(0,a,5))
    for i in lista:
        soma += i
    print(soma)