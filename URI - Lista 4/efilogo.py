#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# b j p s v x z
from sys import stdin


i = 0
while True:
    try:   
        string = ''.join(stdin.readlines())
        intab = "bjpsvxzBJPSVXZ"
        outtab = "fffffffFFFFFFF"
        trantab = string.maketrans(intab,outtab)       
        string = string.translate(trantab))
        saida = ""
  
        # string = input()
        # for i in range(len(letMin)):
        #     s = string.replace(letMin[i],'f')    
        #     string = s
        #     letMai.append(letMin[i].upper())   
        # for i in range(len(letMai)):
        #     s = string.replace(letMai[i],'F')
        #     string = s
        # # for i in range(len(doubleF)):           
        # #     s = string.replace(doubleF[i],doubleF2[i])
        # #     string = s
        # palavras = string.split() 
        # for i in range(len(palavras)):
        #     x1,x2,x3,x4 = 1,1,1,1
        #     while x1 != 0 or x2 != 0 or x3 != 0 or x4 != 0:
        #         x1 = palavras[i].count('ff')
        #         x2 = palavras[i].count('fF')
        #         x3 = palavras[i].count('FF')
        #         x4 = palavras[i].count('Ff')
        #         palavra = palavras[i]
        #         #print(x1,x2,x3,x4,palavra)
        #         for j in range(len(doubleF)):           
        #             s = palavra.replace(doubleF[j],doubleF2[j])
        #             palavra = s
        #         palavras[i] = palavra
        # palavrasFinal = ' '.join(palavras)
        # print(palavrasFinal)
            #string = string +' '+ s
        
    except EOFError:
        break
exit(0)