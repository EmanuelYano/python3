#!/usr/bin/env python3
#-*- coding:utf-8 -*-
n = int(input())
i,tf = 1, 0
while i != 0:
	y = n % 10
	n = n // 10
	y2 = n % 10
	if y == y2:
		i = 0
		tf = 1
	else:
		i=0
if tf == 1:
	print("Contém dois digitos consecutivos %d%d"%(y,y2))
else:
	print("Não contém dois digitos consecutivos.")
exit(0)