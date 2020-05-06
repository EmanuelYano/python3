#!/usr/bin/env python3
#-*- coding:utf-8 -*-
n = int(input())
i = Ni = Np = 0
while i < n:
	num = int(input())
	if num % 2 != 0:
		Ni += 1
	else:
		Np += 1
	i += 1
print("Nºs pares %d; Nºs impares %d."% (Np,Ni))
exit(0)