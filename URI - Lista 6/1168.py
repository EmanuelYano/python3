#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# 1 -> 2
# 4 -> 4
# 7 -> 3
# 8 -> 7
# 2,3,5 -> 5
# 6,9,0 -> 6

n = int(input())

valor = []

for i in range(n):
    valor.append(input())

for i in valor:
    somaLed = 0
    for num in i: 
        if int(num) == 1:
            somaLed += 2
        elif int(num) == 4:
            somaLed += 4
        elif int(num) == 7:
            somaLed += 3
        elif int(num) == 8:
            somaLed += 7
        elif (int(num) == 2) or (int(num) == 3) or (int(num) == 5):
            somaLed += 5
        else: 
            somaLed += 6
    print("%d leds"%somaLed)

exit(0)