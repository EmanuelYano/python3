#!/usr/bin/env python3
#-*- coding: utf-8 -*-

codP, numP, valP = input().split()
codP, numP, valP = int(codP), int(numP),float(valP)
codP2, numP2, valP2 = input().split()
codP2, numP2, valP2 = int(codP2), int(numP2), float(valP2)
totPag = (numP * valP) + (numP2 * valP2)
print("VALOR A PAGAR: R$ %.2f"%totPag)
exit(0)