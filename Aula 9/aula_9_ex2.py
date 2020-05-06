#!/usr/bin/env python3
#-*- coding:utf-8 -*-
def Fib(n):
	j,fi,f2i = 0, 1,1
	if n == 1 or n == 2:
		return 1
	else:
		while j < n-2:
			f3i = f2i
			f2i += fi
			fi = f3i
			j += 1
		return f2i

num = int(input())
print(Fib(num)) 
exit(0)