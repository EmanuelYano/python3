#!/usr/bin/env python3
#-*- coding:utf-8 -*-
"""i = 0
n,x = input().split()
n,x = int(n), int(x)
exp = n
while i < x:
    if i == 0:
        print("1", end=' ')
    elif i == 1:
        print("%d"%n,end=' ')   
    else:
        n = n * exp
        print(n, end=' ')
    i += 1
"""
'''x = input("Está na tomada? ")
if x == "Não":
    print("Ligue na tomada")
else:
    y = input("O monitor está ligando? ")
    if y == "Não":
        print("Arrume o monitor")
    else: 
        print("Arrume o computador")
'''
i = 1
PA,PB,CA,CB = input().split()
PA,PB,CA,CB = int(PA),int(PB),float(CA),float(CB)
while i > 0:
    PA = PA + int(PA * (CA / 100))
    PB = PB + int(PB * (CB / 100))
    print(PA,PB)
    if PA > PB:
        print(i)
        i = -1
    i += 1

exit(0)
