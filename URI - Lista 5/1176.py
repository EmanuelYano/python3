#!/src/bin/env python3
#-*- coding: utf-8 -*-

def fib(n):
	j,fi,f2i = 0, 1,1
	if n == 1 or n == 2:
		return 1
	elif n == 0:
		return 0
	else:
		while j < n-2:
			f3i = f2i
			f2i += fi
			fi = f3i
			j += 1
		return f2i
num = []
k = int(input())

for i in range(k):
	n = int(input())
	num.append(n)
for fibo in num:
	resul = fib(fibo)
	print("Fib(%d) = %d"%(fibo,resul))
exit(0)