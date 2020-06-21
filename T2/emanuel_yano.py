#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#
#Emanuel Ricardo Yano
#Trabalho 2
#Professor: Diego Padilha
#

def guardaSepara(palavra,j):
    palavra2 = ""
    for i in palavra:
        if i.isalpha():
                palavra2 += i.lower()
    hashtags.append((palavra2 + ' ' + str(j)).split())
    if palavra2 not in qtdHashPostada:
        qtdHashPostada.append(palavra2)
        qtdHashPostada.append(1)
    else:
        i = 0
        for repHashtag in qtdHashPostada:
            if repHashtag == palavra2:
                qtdHashPostada[i+1] += 1  
            i += 1 

k = int(input())
for i in range(k):
    hashtags,frases,letraHum,qtdHashPostada = [],[],"a",[]
    j = 0
    print()
    pL = input()
    while letraHum != 'F':
        frase = input().split()
        frases.append([ i for i in frase])
        letraHum = frases[j][0]       
        if letraHum == 'I':
            for palavra in frase:
                for letra in palavra:
                    if letra == "#":
                        guardaSepara(palavra,j)
        #
        elif letraHum == 'P':
            buscar, buscarFraseID = 0, []
            hashtagBusca = (frase[1].lower()).replace("#","")
            while buscar < len(hashtags):
                if hashtagBusca == hashtags[buscar][0]:
                    buscarFraseID.append(int(hashtags[buscar][1]))
                buscar += 1
            for i in buscarFraseID:
                cont = 0
                for resul in frases:
                    if cont == i:
                        print(' '.join(resul[1:]))
                    cont += 1
        #
        elif letraHum == "L":
            for i in range(0,len(qtdHashPostada),2):
                print("#%s %d"%(qtdHashPostada[i],qtdHashPostada[i+1]))
        j +=1

exit(0)