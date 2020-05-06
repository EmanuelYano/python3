#!/usr/bin/env python3
#-*- coding:utf-8 -*-
n = int(input())
i = 1
x = n % 10
n = n // 10
while i != 0:
	x2 = n % 10
	n = n // 10	
	if x == x2 and n == 0:
		print("Possuem o primeiro e último digito iguais.")
		i = 0
	elif n == 0:
		print("Não possui o primeiro e último digito iguais.")
		i = 0


exit(0)