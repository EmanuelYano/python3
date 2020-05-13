#!/usr/bin/env python3
#-*- coding: utf-8 -*-
i = 0
nWords = int(input())
while i < nWords:
    word = input()
    if len(word) > 3:
        print("3")
    else:
        letter = word[0]
        letter2 = word[1]
        letter3 = word[2]
        if letter == 't' and letter2 == 'w' or letter == 't' and letter3 == 'o' or letter2 == 'w' and letter3 == 'o':
            print("2")
        else:
            print("1")
    i += 1
exit(0)