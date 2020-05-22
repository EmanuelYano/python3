#!/src/bin/env python3
#-*- coding:utf-8 -*-

i,soma,k = 1,0,0
lista = input().split()
a = int(lista[0])
while i < len(lista):
    x = int(lista[i])
    if x > 0:
        for k in range(k,int(lista[i])):
            soma += a + k    
    i += 1
print(soma)
exit(0)