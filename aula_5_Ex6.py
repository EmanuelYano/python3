#!/usr/bin/env python3
#-*- coding:utf-8 -*-
a = int(input())
b = int(input())
da = a * 2
dif = abs(a - b)
if (a % 2 == 1 and a < 0 and a < b) or (a < -3) or (da % b == 0) or (b % 2 != 0 and b % a == 0 and b != a) or (dif > 10):
	print("SIM")
else:
	print("NÃO")


exit(0)