#!/usr/bin/env python3
#-*- coding:utf-8 -*-
i = 1
n = int(input())
while i < n+1:
    num, base = input().split()
    if base == "dec":
        print("Case %d:"%i)
        print(str(hex(int(num))).replace('0x',''),"hex")
        print(str(bin(int(num))).replace('0b',''),"bin")
        print()
    elif base == "hex":
        print("Case %d:"%i)
        print(int(num,16),"dec")
        print(str(bin(int(num,16))).replace('0b',''),"bin")
        print()
    elif base == "bin":
        print("Case %d:"%i)
        print(int(num,2),"dec")
        print(str(hex(int(num,2))).replace('0x',''),"hex")
        print()
    i += 1
exit(0)
#https://wiki.python.org.br/ManipulandoStringsComPython strings de python