#!/usr/bin/env python3
#-*- coding: utf-8 -*-
def idade_em_dias(aa,mm,dd): #aa = anos; mm = mes; dd = dias
    if aa == 0 and mm == 0:
        return dd
    else:
        aa *= 365
        mm *= 30
        return aa + mm + dd

aa,mm,dd = input().split()
aa,mm,dd = int(aa), int(mm), int(dd)
print(idade_em_dias(aa,mm,dd))
exit(0)