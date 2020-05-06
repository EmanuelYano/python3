#!/usr/bin/env python3
#-*- coding:utf-8 -*-

def fatorial(n):
    i,k,nx = 1,1,n
    if n == 0:
        return 1
    else:
        while i < nx:
            n = n * k
            k = nx - 1
            nx-=1 
        return n

fat = int(input())
res = fatorial(fat)
print(res)

exit(0)