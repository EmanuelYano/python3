#!/usr/bin/env python3
#-*- coding:utf-8 -*-
n = 0
while True:    
    try:
        corvo = input()
        if corvo == '---':
            n += 0
        elif corvo == '--*':
            n += 1
        elif corvo == '-*-':
            n += 2
        elif corvo == '-**':
            n += 3
        elif corvo == '*--':
            n += 4
        elif corvo == '*-*':
            n += 5
        elif corvo == '**-':
            n += 6
        elif corvo == '***':
            n += 7
        elif corvo == 'caw caw':
            print("%d"%n)
            n = 0
    except EOFError:
        break

exit(0)