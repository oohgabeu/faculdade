# Atividade 01

from random import randint

L = []
for contagem in range(20):
    L.append(randint(1, 100))

print(L)

P = []
for numero in L:
    if numero % 2 == 0:
        P.append(numero)
        
print(P)

soma_pares = 0
for numero in P:
    soma_pares += numero
    
print(f'Soma: {soma_pares}')

cont = 0
for numero in L:
    if numero > 50:
        print(f'Lá vem o homem-macaco!!! [{numero}]')
        cont += 1
        
print(f'Contagem: {cont}')

cont = len(L)
cont02 = 0
for numero in L:
    if numero > 90:
        print(f'Lá vem o homem-macaco!!! [{numero}]')
        break
    cont02 += 1
    
if cont == cont02: print('Receba!!!')
