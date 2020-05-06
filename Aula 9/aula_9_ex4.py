#!/usr/bin/env python3
#-*- coding:utf-8 -*-
def triangular(n):
    mult,num = 1,0
    while num < n:
        num = mult * (mult + 1) * (mult + 2) 
        mult += 1
    if num == n:
        return True
    else:
        return False
numero = int(input())
if triangular(numero) == 1:
    numTri = "é"
else:
    numTri = "não é"
print("Esse numero", numTri ,"triangular")

exit(0)