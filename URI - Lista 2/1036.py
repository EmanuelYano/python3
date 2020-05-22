#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import math
a, b, c = input().split()
a, b, c = float(a), float(b), float(c)
D = b ** 2 - (4 * a * c)
if D < 0 or a == 0:
    print("Impossivel calcular")
else:
    x1 = (-b + (math.sqrt(D))) / (2 * a)
    x2 = (-b - (math.sqrt(D))) / (2 * a)
    print("R1 = %.5f"%x1)
    print("R2 = %.5f"%x2)

exit(0)