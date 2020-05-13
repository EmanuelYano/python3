#!/usr/bin/env python3
#-*- coding:utf-8 -*-

i=0
numeros = []
n = int(input())
while i < n:
    numeros.append(int(input()))
    i += 1
print(numeros[n::-1])

exit(0)