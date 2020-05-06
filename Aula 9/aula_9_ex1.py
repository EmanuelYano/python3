#!/usr/bin/env python3
#-*- coding:utf-8 -*-

n1, op, n2 = input().split()
n1,n2 = int(n1),int(n2)
if op == '+':
	r = n1 + n2
elif op == '-':
	r = n1 - n2
elif op == '*':
	r = n1 * n2
else:
	r = n1 / n2
print(r)

exit(0)