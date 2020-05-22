#!/usr/bin/env python3
#-*- coding:utf-8 -*-
i = 0
numeros = input().split()
seq = ""
while i == 0:
    termo1 = numeros[i]
    for j in numeros:
        if int(termo1) > int(j):
            termo1 = int(j)    
    if str(termo1) not in seq:
        seq = seq  + str(termo1) + ' '
    numeros.remove(str(termo1))
    if len(numeros) == 0:
        i = 1
print(seq)
exit(0)