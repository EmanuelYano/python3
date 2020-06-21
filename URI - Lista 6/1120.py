#!/usr/bin/env python3
#-*- coding:utf-8 -*-
texto = ""
while texto != '0 0':
    lista, lista2 = [], ""
    texto = input()
    if texto != '0 0':
        lista.append([i for i in texto.split()])
        qtdNum = lista[0][1].count(lista[0][0])
        numErro = lista[0][0]
        num = lista[0][1]       
        for i in num:
            if numErro != i:
                lista2 += str(i)
        if (lista2 == "") or (int(lista2) == 0):
            lista = ''
            lista2 = '0'          
        print(int(lista2))
exit(0)