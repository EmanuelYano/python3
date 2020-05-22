#!/usr/bin/env python3
#-*- coding: utf-8 -*-
n1, n2, n3, n4 = input().split()
n1, n2, n3, n4 = float(n1),float(n2),float(n3),float(n4)

m = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10
if m < 5.0:
    print("Media: %.1f"%m)
    print("Aluno reprovado.")
elif m > 7.0:
    print("Media: %.1f"%m)
    print("Aluno aprovado.")
else:
    ne = float(input())
    print("Media: %.1f"%m)
    print("Aluno em exame.")
    print("Nota do exame: %.1f"%ne)
    m2 = (ne + m) /2
    if m2 > 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.") 
    print("Media final: %.1f"%m2)        
exit(0)