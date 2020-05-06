#!/usr/bin/env python3
#-*- covalg: utf-8 -*-
def cedulas(val):
    #1,5,10,20
    vin = val // 20
    val -= vin * 20
    dez = val // 10
    val -= dez * 10
    cin = val // 5
    val -= cin * 5
    hum = val // 1 
    val -= hum * 1
    return hum,cin,dez,vin
#
valor = int(input())
hum,cin,dez,vin = cedulas(valor)
print("%d nota(s) de $1.00"%hum)
print("%d nota(s) de $5.00"%cin)
print("%d nota(s) de $10.00"%dez)
print("%d nota(s) de $20.00"%vin)



exit(0)