#!/usr/bin/env python3
#-*- coding:utf-8 -*-
i,maior,menor = 0,-999999,999999
n_estu = int(input())
while n_estu > i:
	nota = float(input())
	if nota > maior:
		maior = nota
	if nota < menor:
		menor = nota
	i += 1
print("Maior nota: %.2f \n Menor nota: %.2f"%(maior,menor))
exit(0)