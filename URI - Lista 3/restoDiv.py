#!/usr/bin/env python3
#-*- coding: utf-8 -*-

x, y = int(input()), int(input())
if x < y:
	x,y = y,x
y += 1
while y < x:
	if y % 5 == 2 or y % 5 == 3:
		print(y)
	y += 1

exit(0)