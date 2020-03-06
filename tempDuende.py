#!/usr/bin/env python3
#-*- coding: utf-8 -*-
x = int(input())
a,b = input().split(" ")
a = int(a)
b = int(b)
if x >= a + b:
	print("Farei hoje!")
else: 
	print("Deixa para amanha!")
exit(0) 