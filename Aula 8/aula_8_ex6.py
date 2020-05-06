#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#i = 1
def inverter(a):
	resp = 0
	while a != 0:
		y = a % 10
		a //= 10
		resp = resp * 10 + y 
	return resp

n = int(input())
if n == inverter(n):
	print("O número é palíndromo.")
else:
	print("O número não é palíndromo.")
exit(0)