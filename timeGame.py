#!/usr/bin/env python3
#-*- coding: utf-8 -*-
hi,hf = input().split(" ")
hi = int(hi)
hf= int(hf)

if hi == hf:
	print("O JOGO DUROU 24 HORA(S)")
else:
	if hf > hi:
		dur = hf - hi
	else: 
		dur = (24 - hi) + hf
	print("O JOGO DUROU %d HORA(S)"%(dur)) 
exit(0)