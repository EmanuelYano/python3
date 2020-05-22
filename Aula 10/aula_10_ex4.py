#!/usr/bin/env python3
#-*- coding:utf-8 -*-
nDados, i, seqDados, j = [], 0, [], 1

n = int(input())
for i in range(i,n):
    nums = int(input())
    nDados.append(nums)
while j < 7:
    seqDados.append(str(nDados.count(j)))
    j += 1
print(', '.join(seqDados)) 
exit(0)