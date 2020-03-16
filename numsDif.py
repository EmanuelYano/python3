#!/usr/bin/env python3
#-*- coding: utf-8 -*-
a = int(input())
neg,imp,pos,par = 0,0,0,0
if a < 0:
	neg += 1
	if a % 2 != 0:
		imp += 1
	else:
		par += 1
elif a > 0:
	pos += 1
	if a % 2 == 0:
		par += 1
	else:
		imp += 1
else:
	par += 1
b = int(input())
if b < 0:
	neg += 1
	if b % 2 != 0:
		imp += 1
	else:
		par += 1
elif b > 0:
	pos += 1
	if b % 2 == 0:
		par += 1
	else:
		imp += 1
else:
	par += 1
c = int(input())
if c < 0:
	neg += 1
	if c % 2 != 0:
		imp += 1
	else:
		par += 1
elif c > 0:
	pos += 1
	if c % 2 == 0:
		par += 1
	else:
		imp += 1
else:
	par += 1
d = int(input())
if d < 0:
	neg += 1
	if d % 2 != 0:
		imp += 1
	else:
		par += 1
elif d > 0:
	pos += 1
	if d % 2 == 0:
		par += 1
	else:
		imp += 1
else:
	par += 1
e = int(input())
if e < 0:
	neg += 1
	if e % 2 != 0:
		imp += 1
	else:
		par += 1
elif e > 0:
	pos += 1
	if e % 2 == 0:
		par += 1
	else:
		imp += 1
else:
	pos += 1
print("%d valor(es) par(es)"%(par))
print("%d valor(es) impar(es)"%(imp)) 
print("%d valor(es) positivo(s)"%(pos)) 
print("%d valor(es) negativo(s)"%(neg))
exit(0)