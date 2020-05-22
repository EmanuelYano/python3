#!/src/bin/env python3
#-*- coding: utf-8 -*-
lista = []
k = 0
for i in range(100):
    l = float(input())
    lista.append(l)
for j in lista:
    if float(j) <= 10:
        print("A[%d] = %.1f"%(k,j))
    k += 1
exit(0)