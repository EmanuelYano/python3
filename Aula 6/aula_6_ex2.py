#!/usr/bin/env python3
#-*- coding: utf-8 -*-

def maior_3(x,y,z):
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
    return z,y,x

a, b, c = int(input()), int(input()), int(input())
mai, med, men = maior_3(a,b,c)
print(mai, men)
exit(0)