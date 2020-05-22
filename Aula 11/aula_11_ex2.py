#!/usr/bin/env python3
#-*- coding:utf-8 -*-
def remrep(lista):
    for i in lista:
        if i not in lista2:
            lista2.append(i)
lista2 = []
lista = input().split()
remrep(lista)
print(' '.join(lista2))
exit(0)