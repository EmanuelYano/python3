#!/usr/bin/env python3
#-*- coding:utf-8 -*-
def area_triangulo(b,h):
    a = (b * h) / 2
    return a

b, h = float(input()), float(input())
a = area_triangulo(b,h)
print(a)

exit(0)