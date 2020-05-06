#!/usr/bin/env python3
#-*- coding:utf-8 -*-
def quebra(n):
	if n < 10:
		pDig = n
		uDig = n
		meio = 0
		return pDig, uDig, meio
	else:
		i = potDez = 1
		uDig = n % 10
		n = n // 10
		# 
		while i == 1:
			potDez *= 10
			if potDez > n:
				potDez /= 10 
				pDig = n // potDez
				meio = n - (pDig * potDez)
				i = 0
		return pDig, uDig, meio
#
#
n = int(input("Digite um número para descobrir se ele é palíndromo: "))
mid = 12
torf = j = 0
while mid > 9:	
	digP, digU, mid = quebra(n)
	if digP == digU:
		torf += 1 
	else:
		torf -= 1
	j += 1
	n = mid
if torf == j:
	print("Esse número é palíndromo!!!")
else:
	print("Esse número não é palindromo!!!")

exit(0)