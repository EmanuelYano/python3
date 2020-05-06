#!/usr/bin/env python3
#-*- coding:utf-8 -*-
def primo(p):
	i,pos = 1,0
	while i < p:
		if p % i == 0:
			pos += 1
		i+=1
	if pos == 1:
		return True
	else:
		return False
i,som = 0,0
n = int(input())
while i < n:
	num = int(input())
	nPrimo = primo(num)
	if nPrimo == True:
		som += num
	i+=1
print(som)

exit(0)