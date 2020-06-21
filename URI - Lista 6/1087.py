#!/usr/bin/env python3
#-*- coding:utf-8 -*-

pos,true,tabuleiro = [],0,[]
pos.append([int(i) for i in input().split()])
for i in range(4):
    if pos[0][i] == 0:
        true += 1
while true != len(pos[0]):
    for i in range(8):
        tabuleiro.append([0]*8)
        m = pos[0][0] - 1
        n = pos[0][1] - 1
        m2 = pos[0][2] - 1
        n2 = pos[0][3] - 1
        if i == m:
            tabuleiro[m][n] = 1
        if i == m2:
            tabuleiro[m2][n2] = 1

    if (m == m2) and (n == n2):
        print("0")
    elif (m == m2) and (n != n2):
        print("1")
    elif (n == n2) and (m != m2):
        print("1")
    elif abs(m - m2) == abs(n - n2):
        print("1")
    else:
        print("2") 
    
    true,pos,tabuleiro = 0,[],[]
    pos.append([int(i) for i in input().split()])
    for i in range(4):
        if pos[0][i] == 0:
            true += 1



exit(0)