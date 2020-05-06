#!/usr/bin/env python3
#-*- coding:utf-8 -*-
i,maior,dia = 1, -99999,0
# dia 1 = domingo, dia 2 = segunda, ...
while i < 8:
	Qtd_disc = int(input())
	if Qtd_disc > maior:
		maior = Qtd_disc
		dia = i
	i += 1
print(maior,dia)

exit(0)