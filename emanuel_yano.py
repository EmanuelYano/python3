#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#
#Emanuel Ricardo Yano
#Trabalho 1
#Professor: Diego Padilha
#

def pegaDigito(val,loop):
	i,j,numFin,numFin2,passa1vez = 0,0,0,0,0
	while i < loop:
		rst = val % 10
		val //= 10
		numFin = numFin * 10 + rst
		i+=1
		if i == loop and passa1vez == 0:
			val,numFin,i,passa1vez = numFin,0,0,1
	return numFin
def mesmoGrupo(n,grupo):
	i = 0
	while i == 0:
		if grupo == 0:
			if grupo <= 97 or grupo == 0:
				i = 1
				return True
		elif grupo % 4 == 0:
			if grupo == n or grupo-1 == n or grupo-2 == n or grupo-3 == n:
				return True
			else:
				return False
			i = 1
		else:
			while grupo % 4 != 0:
				grupo += 1
def pila(din):
	cem = din // 100
	din =  din - (cem * 100)
	dez = din // 10
	din =  din - (dez * 10)
	hum = din // 1
	return cem,dez,hum
#
v,n,m = 1,1,1
while v != 0 or n != 0 or m != 0:
	v,n,m = input().split()
	v,n,m = int(v), int(n), int(m)
	if v != 0 or n != 0 or m != 0:	
		numDig,mSorteio = pegaDigito(n,2), pegaDigito(m,2)	
		if pegaDigito(n,4) == pegaDigito(m,4):
			money = v * 3000
		elif pegaDigito(n,3) == pegaDigito(m,3):
			money = v * 500
		elif numDig == mSorteio:
			money = v * 50
		elif mesmoGrupo(numDig,mSorteio):
			money = v * 16
		else:
			money = v * 0
		cem,dez,hum = pila(money)
		print("%d %dx100 %dx10 %dx1"%(money,cem,dez,hum))
		
exit(0)