#!/usr/bin/env python3
#-*- coding:utf-8 -*-

def somaAbaixoDiagonal(tam):
    col = tam-1
    s = 0
    for i in range(1,tam):   
        for j in range(col,tam):
            s += M[i][j]
        col -= 1
    return s

M,tam = [],12
op = input()
for i in range(tam):
    L = []
    for j in range(tam):
        L.append(float(input()))
    M.append(L)

if op == "S":
    soma = somaAbaixoDiagonal(tam)
    print("%.1f"%soma)
elif op == "M":
    soma = somaAbaixoDiagonal(tam)
    media = soma / 66
    print("%.1f"%media)


exit(0)