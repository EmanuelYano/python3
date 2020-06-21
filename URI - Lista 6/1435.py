#!/usr/bin/env python3
#-*- coding:utf-8 -*-

def passada_hum(entrada):
    saida = ""
    for i in entrada:
        if i.isalpha():
            saida += chr(ord(i)+3)  
        else:
            saida += i
    return saida

def passada_dois(entrada):    
    return entrada[::-1]

def passada_tres(entrada,n):
    saida = ""
    metade = n // 2
    for i in range(metade,n):
        saida += chr(ord(entrada[i])-1)
    return entrada[:metade] + saida


n = int(input())
for i in range(n):
    entrada = input()
    tam = len(entrada)
    passo_1 = passada_hum(entrada)
    passo_2 = passada_dois(passo_1)
    passo_3 = passada_tres(passo_2,tam)
    print(passo_3)
exit(0)