#!/usr/bin/env python3
#-*- coding:utf-8 -*-
matriz,f = [],2
m = int(input("Linhas: "))
n = int(input("Colunas: "))
print("Matriz:")

for i in range(m):
    matriz.append([int(j) for j in input().split()])

i,k,l,p = 0,0,1,0

while (f != 0) and (m*n != p):
    comp = matriz[i][k]
    f = 2
    for j in range(m):      
        for l in range(n):
            if comp == matriz[j][l]:
                f += -1   
    if k == n-1:
        i += 1
        k = -1 
    k += 1
    p += 1

if (f < 1):
    print("Existe repetições nessa matriz.")
else:
    print("Não existe repetições nessa matriz.")
exit(0)