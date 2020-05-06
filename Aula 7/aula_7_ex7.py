#!/usr/bin/env python3
#-*- coding:utf-8 -*-

n = int(input())
i = sp = si = 0
while i < n:
	n2 = int(input())
	if n2 % 2 == 0:
		sp += n2
	else:
		si += n2
	i += 1
print(sp,si)

exit(0)