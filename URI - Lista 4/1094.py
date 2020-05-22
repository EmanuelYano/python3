#!/usr/bin/env python3
#-*- coding: utf-8 -*-

i,cob,c,r,s = 0,0,0,0,0
n = int(input())
while i < n:
    qt,tp = input().split()
    qt = int(qt)
    cob += qt
    if tp == "C":
        c += qt
    elif tp == "R":
        r += qt
    else:
        s += qt   
    i += 1
print("Total: %d cobaias"%cob)
print("Total de coelhos: %d"%c)
print("Total de ratos: %d"%r)
print("Total de sapos: %d"%s)
print("Percentual de coelhos: %.2f"% (c*100/cob), "%")
print("Percentual de ratos: %.2f"% (r*100/cob), "%")
print("Percentual de sapos: %.2f"% (s*100/cob), "%")


exit(0)