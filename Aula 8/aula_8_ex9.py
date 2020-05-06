#!/usr/bin/env python
# -*- coding: utf-8 -*-

minuscula = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
maiuscula = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numeros = ['1','2','3','4','5','6','7','8','9','0']
pontuacao = ['.',',',';',':','?','/','!','(',')','[',']','{','}','-','+','*','=','_','@','#','$','%','&','§','ª','º']

frase = input("Informe uma frase: ")
esp,minus, maius,num,pontu = 0,0,0,0,0
for c in frase:
	if c == "":
		esp += 1
	if c == "":
		minus += 1
	if c == "":
		maius += 1
	if c == "":
		num += 1
	if c == "":
		pontu += 1
print("A frase tem %d espaços" % (esp))

exit(0)
