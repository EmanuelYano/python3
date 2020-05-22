#!/usr/bin/env python3
#-*- coding:utf-8 -*-
t,f= False,False
d1,d2,d3 = input().split()
d1,d2,d3 = int(d1),int(d2),int(d3)
if d1 > d2 and (d3 == d2 or d3 > d2):
    f = True
elif d1 < d2 and d2 < d3 and abs(d3 - d2) >= abs(d2 -d1):
    f = True
elif d1 > d2 and d2 > d3 and abs(d3 - d2) < abs(d2 - d1):
    f = True
elif d1 == d2 and d2 < d3:
    f =True
elif d1 < d2 and d2 < d3 and abs(d3-d2) < abs(d2-d1): 
    t = True
elif d1 < d2 and d2 <= d3:
    t = True
elif d1 > d2 and d2 > d3 and abs(d3-d2) >= abs(d2-d1):
    t = True
elif d1 == d2 and d2 > d3:
    t = True

if f:
    print(":)")
else:
    print(":(")

exit(0)