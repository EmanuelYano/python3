#!/src/bin/env python3
#-*- coding: utf-8 -*-
lista = []
k = 0
for i in range(10):
    l = int(input())
    lista.append(l)
for j in lista:
    if int(j) <= 0:
        lista[k] = 1
    print("X[%d] = %d"%(k,lista[k]))
    k += 1
exit(0)