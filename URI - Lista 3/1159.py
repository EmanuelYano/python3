#!/usr/bin/env python3
#-*- coding:utf-8 -*-
j = 1
i = s = 0
while j != 0:
	x = int(input())
	j = x
	if x % 2 == 1:
		x += 1
	#s = x 
	while i < 5:
		s += x
		x += 2
		#print(s)
		i += 1
	if j != 0:
		print(s)
	i = s = 0





exit(0)