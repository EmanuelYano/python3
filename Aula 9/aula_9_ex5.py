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

a,b = int(input()),int(input())
mdc = mdc(a,b)
a /= mdc
b /= mdc
print(int(a),"/",int(b))
    
exit(0)