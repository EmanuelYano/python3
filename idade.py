#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = int(input())

if x < 30:
	print("0 ano(s)")
	print("0 mes(es)")
	print(x,"dia(s)")
else:
	d = 0
	a = 0
	m = 0
	if x >= 365:
		a = x // 365
		z = x % 365
		if z >= 30:
			i = z % 30
			z = z // 30
			m = z
			d = i
		else:
			d = z
	else:
		m = x // 30
		d = x % 30
	print(a,"ano(s)")
	print(m,"mes(es)")
	print(d,"dia(s)")
exit(0)