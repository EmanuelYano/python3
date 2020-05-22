#!/src/bin/env python3
#-*- coding: utf-8 -*-
v = int(input())
lista = []
for i in range(1000):
    for k in range(0,v):
        lista.append(k)
for j in range(1000):
    print("N[%d] = %d"%(j,lista[j]))
exit(0)