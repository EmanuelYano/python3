#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'''i = 1
x,y = input().split()
x,y = int(x), int(y)

while i <= y:
	print(i, end=' ')
	if i % x == 0: 
		if i != y:
			print()			
	i += 1'''


i = 1
x,y = input().split()
x,y = int(x), int(y)

while i <= y:
    if i % x == 0: 
        print(i)     
    else: 
        print(i, end=' ') 
    i += 1
exit(0)