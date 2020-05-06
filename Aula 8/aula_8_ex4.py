#!/usr/bin/env python3
#-*- coding:utf-8 -*-
i = 1
s = ''
n = int(input("Digite um número (na base decimal) para ser convertido em binário: "))
j = n
while i != 0:
	r = n % 2
	n //= 2
	s += str(r) 
	if n==1 or n==0:
		i = 0
		s += str(n)
print("o numero que",j,"na base binária é:",s[::-1])

	

exit(0)