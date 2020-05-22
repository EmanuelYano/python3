#!/usr/bin/env python3
#-*- coding:utf-8 -*-

n,m = input().split()
n,m = int(n),int(m)
while m != 0 or n != 0:   
    som = m + n
    print(str(som).replace('0',''))
    n,m = input().split()
    n,m = int(n),int(m)

exit(0)