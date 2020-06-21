#!/usr/bin/env python3
#-*- coding:utf-8 -*-

lista = []

n = int(input())

for t in range(n):
    lista.append([i for i in input().split()])

for i in range(n):   
    bla = 0 
    if len(lista[i][1]) <= len(lista[i][0]):        
        tam_num = len(lista[i][1])
        num1 = lista[i][0]
        num2 = lista[i][1]
        num1 = num1[::-1]
        num2 = num2[::-1]
        #print(num1,",",num2)
        for k in range(tam_num-1,-1,-1):
            
            if num1[k] == num2[k]:
                bla += 1 
        if bla == len(num2):
            print("encaixa")
        else:
            print("nao encaixa")
    else:
        print("nao encaixa")


exit(0)