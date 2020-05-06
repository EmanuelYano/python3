#!/usr/bin/env python3
#-*- coding:utf-8 -*-

n = int(input())
i = sp = sn = 0
while i < n:
	n2 = int(input())
	if n2 > 0:
		sp += 1
	else:
		sn += 1
	i += 1
print(sp,sn)

exit(0)