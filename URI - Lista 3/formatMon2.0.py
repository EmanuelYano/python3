#!/usr/bin/env python3
#-*- coding:utf-8 -*-
def inverter(din):
	return din[::-1]

while True:
	try:
		dol, cent = int(input()), int(input())
		din = str(dol)
		numF,i = '',0
		if dol == 0:
			if cent < 10 :
				print("$0.0%d"%cent)
			else:
				print("$0.%d"%cent)
		else:
			din = inverter(din)
			for car in din:
				if i % 3 == 0 and i != 0:
					numF += ','
				#car = str(car)
				numF += car
				i += 1
				#print(car)
			if cent < 10:
				cent = "0" + str(cent)
			numF = "$" + inverter(numF) + "." + str(cent)
			print(numF)
	except EOFError:
		break
exit(0)