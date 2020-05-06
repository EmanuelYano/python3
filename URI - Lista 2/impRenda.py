#!/usr/bin/env python3
#-*- coding: utf-8 -*-
sal = float(input())
if sal <= 2000.00:
	print("Isento")
elif 2000.01 <= sal <= 3000.00:
	imp = (sal - 2000.00) * 0.08
	print("R$ %.2f"% imp)
elif 3000.01 <= sal <= 4500.00:
	imp = (1000.00 * 0.08) + ((sal - 3000.00) * 0.18)
	print("R$ %.2f"% imp)
else:
    imp = (1000.00 * 0.08 + 1500.00 * 0.18) + ((sal - 4500.00) * 0.28) 
    print("R$ %.2f"% imp)
exit(0)