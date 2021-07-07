import sys

lista = []
for i in range(100, 1000):
    for j in range(100, 1000):
        a = i * j
        if str(a) == str(a)[::-1] and a not in lista:
            lista.append(a)
lista.sort()
q = len(lista)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    for i in range(q - 1, -1, -1):
        if lista[i] < n:
            print(lista[i])
            break