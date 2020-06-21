#!/src/bin/env python3
#-*- coding: utf-8 -*- 

n = int(input("Digite o número de linhas: ")) 
m = int(input("Digite o número de colunas: "))
A = []
print("Digite a matriz:")
for i in range(n):   
    A.append([int(j) for j in input().split()])
compRow,compCol = [],[]
for i in A:
    eh = 0
    for k in i:
        if 0 <= k <= 1: 
            if k == 1:
                eh += 1
    compRow.append(eh)
for i in range(m):
    ehh = 0
    for j in range(n):
        if A[j][i] == 1:
            ehh += 1
    compCol.append(ehh) 
if (compRow.count(1) != n) and (compCol.count(1) != m):
    print("Não é uma matrtiz de permutação!!")
else:
    print("É uma matriz de permutação!!!")
exit(0)