#!/usr/bin/env python3
#-*- coding: utf-8 -*-

matriz,matrizTrans = [],[]

m = int(input("Linhas: "))
n = int(input("Colunas: "))
print("Matriz:")

for i in range(m):
    matriz.append([float(j) for j in input().split()])

for j in range(n):
    listaAux = []
    for l in range(m):
        listaAux.append(matriz[l][j])
    matrizTrans.append(listaAux)

for i in range(n):
    for j in range(m):
        print(matrizTrans[i][j], end=' ')
    print()
    
exit(0)