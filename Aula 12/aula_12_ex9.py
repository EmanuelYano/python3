#!/usr/bin/env python3
#-*- coding:utf-8 -*-

def linha(A,i):
    for num in range(1,len(A)+1):
        if num not in A[i]:
            return False
    return True

def coluna(A,j):
    coluna = []
    for l in range(len(A)):
        coluna.append(A[l][j])
    for num in range(1,len(A)+1):
        if num not in coluna:
            return False
    return True

A, latino = [], 0
n = int(input("Digite o número das linhas/colunas: "))

for j in range(n):
    A.append([int(i) for i in input().split()])

for i in range(n):
    if linha(A,i):
        latino += 1
    else:
        latino -= 1
    j = i
    if coluna(A,j):
        latino += 1
    else:
        latino -= 1

if latino == (n*2):
    print("É um quadrado de ordem latina!!")
else:
    print("Não é um quadrado de ordem latina!!")
exit(0)