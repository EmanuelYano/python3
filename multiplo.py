#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x,y = input().split(" ")
x=int(x)
y=int(y)
if x < y:
	if y % x == 0:
		print("Sao Multiplos")
	else:
		print("Nao sao Multiplos")
else:
	if x % y == 0:
		print("Sao Multiplos")

	else:
		print("Nao sao Multiplos")


exit(0)