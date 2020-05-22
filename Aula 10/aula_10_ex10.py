#!/usr/bin/env python3
#-*- coding:utf-8 -*-

i = 0
numeros = input().split()
seq,rep = "",[]
while len(numeros) != 0:
    termo1 = numeros[i]
    for j in numeros:
        if int(termo1) > int(j):
            termo1 = int(j)    
    if str(termo1) not in seq:
        seq = seq  + str(termo1) + ' '
    elif str(termo1) not in rep:
        rep.append(str(termo1))
    numeros.remove(str(termo1))
print(' '.join(rep))
exit(0)