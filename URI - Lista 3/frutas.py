#!/usr/bin/env python3
#-*- coding:utf-8 -*-
mKg = mBrl = 0
i = 1
n = int(input())
while i <= n:
	val = float(input())
	frutas = input()
	nFru = 1
	for crtr in frutas:
		if crtr == ' ':
			nFru += 1
	print("day %d: %d kg"%(i,nFru))
	mKg += nFru
	mBrl += val
	i += 1
mKg /= n
mBrl /= n
print("%.2f kg by day"%(mKg))
print("R$ %.2f by day"%(mBrl))
exit(0)