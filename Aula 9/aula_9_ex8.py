#!/usr/bin/env python3
#-*- coding:utf-8 -*-

prec = float(input("Digite o valor de precisão: "))

x,i,pi_ant = 3,0,8
pi = 4 - 4/x


while abs(pi_ant - pi) > prec:
	pi_ant = pi
	x += 2
	if i % 2 == 0:
		pi += 4/x
	else:
		pi -= 4/x
	i += 1

print("PI = %.4f"%pi_ant)  
exit(0)