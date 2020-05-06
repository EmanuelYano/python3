#!/usr/bin/env python3
#-*- coding:utf-8 -*-
def div1000(dol):
	rst = dol % 1000
	quoc = dol // 1000
	if dol > 100000000:
		rst = dol % 1000000
		quoc = dol // 1000000

	return rst,quoc

'''dol, cent = int(input()), int(input())
i = potDez = 1
j, qtdZeros, potDez2 = 0,0,1
dolAux = dol'''
while True:
	try: 
		dol, cent = int(input()), int(input())
		i = potDez = 1
		j, qtdZeros, potDez2 = 0,0,1
		dolAux = dol
		if dol >= 1000:
			while i > 0:
				potDez *= 10
				if potDez > dol:
					potDez //= 10
					potDez2 = potDez
					i = -1
			while potDez > 1:
				potDez //= 10
				qtdZeros += 1
			if qtdZeros == 3 or qtdZeros == 6 or qtdZeros == 9 or qtdZeros == 12:
				#print("corno")
				pDig = dol // potDez2
				print("$%d"%(pDig),end='')
				pDig *= potDez2
				dol -= pDig
				#print("\n",pDig, dol, potDez2)		
				if dol <= 999:
					if dol < 100 and dol >= 10:
						print(",0%d"%(dol), end='')
					elif dol < 10 and dol >= 0:
						print(",00%d"%(dol), end='')
						if dolAux >= 1000000 and dolAux < 1000000000 and dol == 0:
							print(",00%d"%(dol), end='')
						elif dolAux >= 1000000000 and dol == 0:
							print(",00%d"%(dol), end='')
							print(",00%d"%(dol), end='')
					else:
						print(",%d"%(dol), end='')
				else:
					while dol > 999:
						dol2, dol = div1000(dol)
						#print('\n',dol2, dol)
						if dol < 100 and dol >= 10:
							print(",0%d"%(dol), end='')
						elif dol < 10 and dol >= 0:
							print(",00%d"%(dol), end='')
						else:
							print(",%d"%(dol), end='')
						dol = dol2
					if dol2 < 100 and dol2 >= 10:
						print(",0%d"%(dol2), end='')
					elif dol2 < 10 and dol2 >= 0:
						print(",00%d"%(dol2), end='')
					else:
						print(",%d"%(dol2), end='')
			elif qtdZeros == 4 or qtdZeros == 7 or qtdZeros == 10 or qtdZeros == 13:
				#print("corno2")
				potDez2 //= 10
				pDig = dol // potDez2
				dol = dol - (pDig * potDez2)
				print("$%d"%(pDig), end='')
				if dol > 999:
					while dol > 999:
						dol2, dol = div1000(dol)
						if dol < 100 and dol >= 10:
							print(",0%d"%(dol), end='')
						elif dol < 10 and dol >= 0:
							print(",00%d"%(dol), end='')
						else:
							print(",%d"%(dol), end='')
						dol = dol2
					if dol2 < 100 and dol2 >= 10:
						print(",0%d"%(dol2), end='')
					elif dol2 < 10 and dol2 >= 0:
						print(",00%d"%(dol2), end='')
					else:
						print(",%d"%(dol2), end='')
				else:
					if dol < 100 and dol >= 10:
						print(",0%d"%(dol), end='')
					elif dol < 10 and dol >= 0:
						print(",00%d"%(dol), end='')
						#print("Fodase")
						if dolAux > 10000 and dolAux <= 10000000 and dol == 0:
							print(",00%d"%(dol), end='')

						elif dolAux >= 10000000000 and dol == 0:
							print(",00%d"%(dol), end='')
							print(",00%d"%(dol), end='')
					else:
						print(",%d"%(dol), end='')
			else:
				#print("corno 3")
				potDez2 //= 100
				pDig = dol // potDez2
				#print(pDig, dol, potDez2)
				dol = dol - (pDig * potDez2)
				#print(dol)
				print("$%d"%(pDig), end='')
				if dol > 999:
					#print("aki 1")
					while dol > 999:
						#print("aki 2")
						dol2, dol = div1000(dol)
						if dol < 100 and dol >= 10:
							print(",0%d"%(dol), end='')
						elif dol < 10 and dol >= 0:
							print(",00%d"%(dol), end='')
						else:
							print(",%d"%(dol), end='')
						dol = dol2
					if dol2 < 100 and dol2 >= 10:
						print(",0%d"%(dol2), end='')
					elif dol2 < 10 and dol2 >= 0:
						print(",00%d"%(dol2), end='')
					else:
						print(",%d"%(dol2), end='')
				else:
					if dol < 100 and dol >= 10:
						print(",0%d"%(dol), end='')
					elif dol < 10 and dol >= 0:
						print(",00%d"%(dol), end='')
						if dolAux > 100000 and dolAux <= 100000000 and dol == 0:
							print(",00%d"%(dol), end='')
						elif dolAux >= 100000000000 and dol == 0:
							print(",00%d"%(dol), end='')
							print(",00%d"%(dol), end='')
					else:
						print(",%d"%(dol), end='')
			if cent < 10:
				print(".0%d"%(cent), end='')
			else:
				print(".%d"%(cent), end='')
		else:
			if cent < 10:
				print("$%d.0%d"%(dol,cent), end = '')
			else:
				print("$%d.%d"%(dol,cent), end = '')
		print()
	except EOFError:
		break 


exit(0)