#!/usr/bin/env python3
#-*- coding:utf-8 -*-
i = j = 0
while i < 7:
	md = int(input())
	if md < 0:
		j +=1
	i += 1
print("%d dias da semana ficaram com uma temperatura abaixo de zero."%j)


exit(0)