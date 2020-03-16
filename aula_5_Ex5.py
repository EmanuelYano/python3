#!/usr/bin/env python3
#-*- coding:utf-8 -*-
a = int(input())
b = int(input())
if (a % 2 == 0 and a > 0 and a % b == 0) or (b % 2 == 1 and b % a == 0 and b != a):
	print("SIM")
else:
	print("NÃO")	

exit(0)