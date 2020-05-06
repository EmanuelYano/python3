#!/usr/bin/env python3
#-*- coding: utf-8 -*-
#1-15;2-18;3-20
def num_lampadas(classe,larg,comp):
    if classe == 1:
        ar = larg * comp
        num_L = (ar * 15) / 60
    elif classe == 2:
        ar = larg * comp
        num_L = (ar * 18) / 60
    else:
        ar = larg * comp
        num_L = (ar * 20) / 60
    return num_L, ar 
classe,larg,comp = int(input()),float(input()), float(input())
lamp, ar = num_lampadas(classe,larg,comp)
print("Área: %.2f \n Número de lâmpadas: %d"% (ar,round(lamp)))
exit(0)