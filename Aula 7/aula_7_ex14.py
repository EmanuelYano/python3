#!/usr/bin/env python3
#-*- coding:utf-8 -*-
i, j, x = 0, 0, 0
n = int(input())
while n > i:
	seq = int(input())
	if seq > x:
		j += 1
		x = seq
	i += 1
if j == n:
	print("Sequência em ordem crescente.")
else:
	print("Sequência não está em ordem crescente.")


exit(0)