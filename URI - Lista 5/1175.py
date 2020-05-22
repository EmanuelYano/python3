#!/src/bin/env python3
#-*- coding: utf-8 -*-
lista,lista2 = [],[]
k = 0
for i in range(20):
    l = int(input())
    lista.append(l)
lista.reverse()
for j in lista:
    print("N[%d] = %d"%(k,lista[k]))
    k += 1
exit(0)