#!/usr/bin/env python3
#-*- coding:utf-8 -*-
def mdc(a,b):
	r = 1
	if a < b:
		a,b = b,a		
	while r != 0:
	    r = a % b
	    a,b = b,r
	return a
n = int(input())
i = resp = 0
while i < n:
	num = int(input())
	if i == 0:
		num2 = num
	if resp != 0:
		num2 = resp
	if i >= 1:
		resp = mdc(num,num2)
	i += 1
print(resp)
exit(0)