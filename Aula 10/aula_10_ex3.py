#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#from random import randint  #função randint(a,b)

#val = [int(i) for v in input().split()]
i = 0
gab = input().split()
n = int(input())
while i < n:
	acertos = 0
	carResp = input().split()
	for	j in range(len(gab)):
		if gab[j] == carResp[j]:
			acertos += 1
	i += 1
	print(acertos)
exit (0)

