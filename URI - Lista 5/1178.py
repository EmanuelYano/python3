#!/src/bin/env python3
#-*- coding: utf-8 -*-
lista = []
k = 0
l = float(input())
for j in range(100):   
    lista.append(l)
    l /= 2
for m in lista:
    print("N[%d] = %.4f"%(k,m))
    k += 1
exit(0)