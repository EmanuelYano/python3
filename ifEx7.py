#!/usr/bin/env python3
#-*- coding:utf-8-*-
x = int(input())
y = int(input())
z = int(input())
if x > y and x > z:
	#x=-999999, y=0, z=9999
	if y < z:
		z,y,x = x,z,y
		#x , z, y 
	else:
		z,y,x = x,y,z
		#x, y, z
if x < y and x < z:
	if y > z:
		z,y,x = y,z,x
		#y, z, x
	else:
		z,y,x = z,y,x
		#z, y, x
if x > y and x < z:
	if z > y:
		z,y,x = z,x,y
		#z, x, y
if x < y and x > z:
	if z < y:
		z,y,x = y,x,z
		#y, x, z
print(z,y,x)
exit(0)