#!/usr/bin/env python3
#-*- coding:utf-8 -*-
i,cMax,compMax = 0,-999,1
n = int(input())
while i < n:
	seqCres = int(input())
	if i > 0:
		if seqCres > seqCres2:
			compMax += 1
		else:
			if compMax > cMax:
				cMax = compMax 				
			compMax = 1	
	seqCres2 = seqCres
	i += 1
print(cMax)

exit(0)