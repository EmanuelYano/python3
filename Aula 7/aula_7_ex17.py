#!/usr/bin/env python3
#-*- coding:utf-8 -*-
l = m = 0
n, i, j = int(input()), int(input()), int(input())
while l < n:
	k = 1
	while k != 0:
		if m % i == 0 or m % j == 0:
			k = 0
			print(m)
		m += 1
	l += 1

exit(0)