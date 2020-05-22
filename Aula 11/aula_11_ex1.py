#!/usr/bin/env python3
#-*- coding:utf-8 -*-
def subconjunto(A,B):
    j = 0
    for i in A:
        if i not in B:
            j += 1
    if j != 0:
        return False
    else:
        return True 
a = input("Digite o primeiro conjunto: ").split()
b = input("Digite o segundo conjunto: ").split()
if subconjunto(a,b) and subconjunto(b,a):
    print("Esses conjuntos são iguais.")
else:
    print("Esses conjuntos não são iguais.")
exit(0)