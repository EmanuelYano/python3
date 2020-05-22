#!/usr/bin/env python3
#-*- coding: utf-8 -*-
i = 0
nCasos = int(input())
while i < nCasos:
	j = k = 0
	nPessoas = int(input())
	while j < nPessoas:
		idioma = input()
		if j == 0:
			idioma2 = idioma
		if idioma2 == idioma:
			k += 1
		else:
			k -= 1
		j += 1
	if k == nPessoas:
		print(idioma)
	else:
		print("ingles")

	i += 1

exit(0)