#!/usr/bin/env python3 
#-*- coding: utf-8 -*-
s=0
x, y = int(input()), int(input())
if x < y:
	x,y = y,x
while y <= x:
	if y % 13 != 0:
		s += y		
	y += 1
print(s)

exit(0)