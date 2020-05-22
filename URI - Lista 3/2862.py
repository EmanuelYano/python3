#!/usr/bin/env python3
#-*- coding: utf-8 -*-

i = 0
c = int(input())
while i < c:
	lvlEner = int(input())
	if lvlEner > 8000:
		print("Mais de 8000!")
	else:
		print("Inseto!")

	i += 1

exit(0)