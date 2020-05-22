#!/usr/bin/env python3
#-*- coding: utf-8 -*-

val = int(input())
val1 = val
cem = val // 100
val = val - (cem * 100)
cinq = val // 50
val = val - (cinq * 50)
vin = val // 20
val = val -(vin * 20)
dez = val // 10
val = val - (dez * 10)
cin = val // 5
val = val - (cin * 5)
dois = val // 2
val = val - (dois * 2)
hum = val // 1
val = val - (hum * 1) 



print("%d"%val1)
print("%d nota(s) de R$ 100,00"%int(cem))
print("%d nota(s) de R$ 50,00"%int(cinq))
print("%d nota(s) de R$ 20,00"%int(vin))
print("%d nota(s) de R$ 10,00"%int(dez))
print("%d nota(s) de R$ 5,00"%int(cin))
print("%d nota(s) de R$ 2,00"%int(dois))
print("%d nota(s) de R$ 1,00"%int(hum))
exit(0)