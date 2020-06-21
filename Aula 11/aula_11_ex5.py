#!/usr/bin/env python3
#-*- codinf:utf-8 -*-
def elimina(C, i):
    for j in C:
        if ((j % i) == 0) and (j > i):
            C.remove(j)        
num = int(input())
i, C,B = 2, [],[]
C = list(range(2,num))
while i < (num ** (1/2)):
    elimina(C,i)
    i += 1
print(*C)
exit(0)