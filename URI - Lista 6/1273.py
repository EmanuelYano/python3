#!/usr/bin/env python3
#-*- coding:utf-8 -*-
n = int(input())
while n != 0:
    palavras,maior = [],-99999
    for i in range(n):
        palavras.append(input())
        if len(palavras[i]) > maior:
            maior = len(palavras[i])
    formatacao = "%" + str(maior) +"s"
    for j in palavras:
        print(formatacao%j)
    
    n = int(input())
    if n != 0:
        print()
exit(0)