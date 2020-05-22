#!/usr/bin/env python3
#-*- coding:utf-8 -*-
def fatorial(n):
    if n == 0:
        return 1
    else:
        for i in range(1,n):
        	n *= i  
        return n
while True:
	try:
		m,n = input().split()
		m,n = int(m), int(n)
		fat = fatorial(m)
		fat2 = fatorial(n)
		resp = fat + fat2
		print(resp)
	except EOFError:
		break
exit(0)