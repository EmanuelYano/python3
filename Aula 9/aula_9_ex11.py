#!/usr/bin/env python3
#-*- coding:utf-8 -*-
def inverter(a):
    resp = 0
    while a != 0:
	    y = a % 10
	    a //= 10
	    resp = resp * 10 + y 
    return resp

j = 0
k = int(input())
while j < k:
    n = int(input())
    i = 0
    while i < 1000:
        nInv = inverter(n)
        if n == nInv:
            print("%d %d"%(i,nInv))
            i = 1001
        elif i == 999:
            print("1000 ??")
        else:
            n += nInv
        i += 1
    j += 1

exit(0)
