#!/usr/bin/env python3
#-*- coding: utf-8 -*-
a = int(input())
neg,imp,pos,par = 0,0,0,0
if a < 0 and a%2 != 0:
	neg += 1
	imp += 1
else:
	pos += 1
	par += 1
b = int(input())
if b < 0 and b%2 != 0:
	neg += 1
	imp += 1
else:
	pos += 1
	par += 1
c = int(input())
if c < 0 and c%2 != 0:
	neg += 1
	imp += 1
else:
	pos += 1
	par += 1
d = int(input())
if d < 0 and d%2 != 0:
	neg += 1
	imp += 1
else:
	pos += 1
	par += 1
e = int(input())
if e < 0 and e%2 != 0:
	neg += 1
	imp += 1
else:
	pos += 1
	par += 1

print(par,imp,"\n",pos,neg)
exit(0)