#what is the largest prime factor of N?
import sys
primos = [2,3,5,7]
def acheiPrimo(x):
    mark = 0
    for i in primos:
        if x%i==0:
            pass
        else:
            mark += 1
    if mark == len(primos):
        primos.append(x)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    lista = list(range(2,n+1))
    for i in lista:
        acheiPrimo(i)
    maior = 0
    for a in primos:
        if n%a==0 and a>maior:
            if a == 1:
                maior = n
            else:
                maior = a
    print(maior)