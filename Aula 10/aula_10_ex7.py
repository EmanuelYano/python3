#!/usr/bin/env python3
#-*- coding:utf-8 -*-
i = 0
numeros = input().split()
termo1 = numeros[0]
for j in numeros:
    if int(j) < int(termo1):
        termo1 = int(j)
print(termo1)
exit(0)