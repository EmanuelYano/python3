#!/usr/bin/env python3
#-*- coding:utf-8 -*-
i,k,m = 0,0,0
numeros = input("Digite a sequência para verificação: ").split()
seq,somas = [],[]
while len(numeros) != 0:
    nMin = nMax = numeros[i]
    for j in numeros:
        if int(nMin) > int(j):
            nMin = int(j)  
        if int(nMax) < int(j):
            nMax = int(j)
    som = int(nMax) + int(nMin)
    somas.append(som)
    numeros.remove(str(nMin))
    numeros.remove(str(nMax))
for l in somas:
    if l == somas[0]:
        m += 1
    else:
        m -= 1
if len(somas) == m:
    print("A sequência é balanceada!!!")
else:
    print("A sequência não é balanceada!!!")     
exit(0)