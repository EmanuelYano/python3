#!/usr/bin/env python3
#-*- coding: utf-8 -*-
x = int(input())
h = 0
if x <= 59:
	print("0:0:%d"%(x))	
else:
 	m = x // 60
 	s = x % 60
 	if m > 59:
 		h = m // 60
 		m = m % 60 		
 	print("%d:%d:%d"%(h,m,s))

exit(0)