#!/usr/bin/env python3
#-*- coding:utf-8 -*-

cad1, cad2 = input().lower(), input().lower()
if cad1 > cad2:
    print("1")
elif cad1 < cad2:
    print("-1")
else:
    print("0")


exit(0)