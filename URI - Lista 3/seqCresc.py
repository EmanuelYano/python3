#!/usr/bin/env python3
#-*- coding:utf-8 -*-
j = 1
while j > 0:
	i = 1
	x = int(input())
	if x != 0:
		while i <= x:
			print(i, end=' ')
			i += 1
	else:
		j = 0
	if x != 0:	
		print()
exit(0)

"""

#!/usr/bin/env python3
#-*- coding:utf-8 -*-
j = 1
while j > 0:
    i = 1
    x = int(input())
    if x != 0:
        string = ""
        while i <= x:
            if(i == 1):
              string = str(i)
            else:
              string =  string + " " + str(i) 
            i += 1
    else:
        j = 0
    if x != 0:  
        print(string)
exit(0)

"""