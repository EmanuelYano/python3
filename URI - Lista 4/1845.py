#!/usr/bin/env python3
#-*- coding:utf-8 -*-
from sys import stdin

string = ''.join(stdin.readlines())
intab = "bjpsvxzBJPSVXZ"
outtab = "fffffffFFFFFFF"
trantab = string.maketrans(intab,outtab)       
string = string.translate(trantab)
saida = ""
ant = ""
for i in string:
    if (i == "f" or i == "F") and  (ant != "f" and ant != "F"):
        saida += i
        #print("entrei", i)
    elif i != "f" and i != "F":
    	saida += i
    ant = i
    #print(ant)
print(saida, end="")
exit(0)