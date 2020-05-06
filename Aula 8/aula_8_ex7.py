#!/usr/bin/env python3
#-*- coding:utf-8 -*-
i, qtdSeq,numSeq2 = 1,0,-1
n = int(input())
while i <= n:
	numSeq = int(input())
	if numSeq != numSeq2:
		qtdSeq += 1	
	numSeq2 = numSeq
	i += 1
print(qtdSeq)

exit(0)