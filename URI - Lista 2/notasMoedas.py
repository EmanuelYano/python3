#!/usr/bin/env python3
#-*- coding: utf-8 -*-
val = float(input())
val1 = val
#notas
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
#print(val)

#moedas
hum = val // 1
val = val - (hum * 1) 
val *= 100
cinqC = val // 50
val -= int(cinqC * 50)
vin5C = val // 25
val -= int(vin5C * 25)
#val = round(val,2)
dezC = val // 10
val -= int(dezC * 10)
#val = round(val,2)
cinC = val // 5
val -= int(cinC * 5)
val = round(val, 2)
#print(val)
humC = int(val // 1)
val -= humC * 1

print("NOTAS:")
print("%d nota(s) de R$ 100.00"%int(cem))
print("%d nota(s) de R$ 50.00"%int(cinq))
print("%d nota(s) de R$ 20.00"%int(vin))
print("%d nota(s) de R$ 10.00"%int(dez))
print("%d nota(s) de R$ 5.00"%int(cin))
print("%d nota(s) de R$ 2.00"%int(dois))
print("MOEDAS:")
print("%d moeda(s) de R$ 1.00"%int(hum))
print("%d moeda(s) de R$ 0.50"%int(cinqC))
print("%d moeda(s) de R$ 0.25"%int(vin5C))
print("%d moeda(s) de R$ 0.10"%int(dezC))
print("%d moeda(s) de R$ 0.05"%int(cinC))
print("%d moeda(s) de R$ 0.01"%int(humC))
exit(0)