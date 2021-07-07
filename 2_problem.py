import sys

def generateFibonnaci(a):
    serie = [1,2]
    while serie[-1] < a:
        serie.append(serie[-1] + serie[-2])
    serie.pop()
    return serie

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    lista = generateFibonnaci(n)
    soma = 0
    for i in lista:
        if i%2==0:
            soma += i
    print(soma)