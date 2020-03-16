#!/usr/bin/env python3
#-*- coding: utf-8 -*-
sal = float(input())
if sal <= 2000.00:
	print("Isento")
elif 2000.01 <= sal <= 3000.00:
	imp = (sal - 2000.00) * 0.08
	print("R$",imp)
elif 3000.01 <= sal <= 4500.00:
	imp = (1000.00 * 0.08) + ((sal - 3000.00) * 0.18)
print(imp) 
exit(0)