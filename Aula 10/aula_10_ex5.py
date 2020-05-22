#!/usr/bin/env python3
#-*- coding:utf-8 -*-
nRoleta, i, seqRoleta, j = [], 0, [], 0

n = int(input())
for i in range(i,n):
    nums = int(input())
    nRoleta.append(nums)
while j < 37:
    seqRoleta.append(str(nRoleta.count(j)))
    j += 1
print(', '.join(seqRoleta)) 
exit(0)