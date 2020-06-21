#!/usr/bin/env python3
#-*- codinf:utf-8 -*-
def uns(lista):
    i, difLista,k ,ant_lista= 0, [],0, 0
    l = [0] * (len(lista)-1)
    while k < len(lista):
        dif = ant_lista - lista[k] 
        if k >= 1:
            difLista.append(abs(dif))
        ant_lista = lista[k]
        k += 1
    while len(difLista) > 0:
        for j in difLista:
            i = 0
            while i < len(l):
                if i == int(j)-1:
                    l[i] += 1 
                    difLista.remove(j)                   
                i += 1
        if j > len(l):
            difLista.remove(j)
    if l.count(1) != len(l):
        return False
    else: 
        return True 

lista = input().split()
lista = [int(i) for i in lista]

if not uns(lista):
    print("Essa sequência não é cheia!!!")
else:
    print("Essa sequência é cheia!!!")



exit(0)