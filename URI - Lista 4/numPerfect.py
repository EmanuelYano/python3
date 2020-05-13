#!/usr/bin/env python3
#-*- coding:utf-8 -*-
def somDiv(n):
    s,i = 0,1
    while i < n:
        if n % i == 0:
            s += i
        i += 1
    return s
i = 0
n = int(input())
while i < n:
    x = int(input())
    if somDiv(x) == x:
        print("%d eh perfeito"%x)
    else:
        print("%d nao eh perfeito"%x) 
    i += 1

exit(0)