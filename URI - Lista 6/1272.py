#!/usr/bin/env python3
#-*- coding:utf-8 -*-

n = int(input())
cadernoCodigos = []
for i in range(n):
    cadernoCodigos.append([input()])

palavra =  ""
for i in cadernoCodigos:   
    for j in i:
        cadernoCodigos2,msgOculta,palavra = [],"",""       
        for k in range(len(j)):
            if j[k] != " ":
                palavra += j[k]                             
            elif (j[k] == " ") or (palavra != ""):
                if (palavra != ""):
                    cadernoCodigos2.append([palavra])
                palavra = ""
            if len(j) == k+1:
                cadernoCodigos2.append([palavra])      
        for l in range(len(cadernoCodigos2)):
            decodificar = cadernoCodigos2[l][0]
            if decodificar != "":
                msgOculta += decodificar[0]
        print(msgOculta)
exit(0)