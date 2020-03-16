#!/usr/bin/env python3
#-*- coding: utf-8 -*-
nome = input()
sal = float(input())
tv = float(input())

com = tv * 0.15
salT = com + sal
print("TOTAL = R$ %.2f" % salT)
exit(0)