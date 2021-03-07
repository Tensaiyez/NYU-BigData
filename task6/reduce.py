#!/usr/bin/env python

import sys
import string

arr=[]
curt = None
count = 1


for line in sys.stdin:
        line = line.strip()
        key, num = line.split('\t', 1)

        if curt == key:
                count+=1
        elif curt:
		id,st=curt.split(',',1)
		arr.append((id,st,count))
		curt=key
		count=1
	else:
		curt=key
		count=1


arr = sorted(arr, key = lambda x: x[2],reverse=True)

for i in range(20):
    print(arr[i][0]+ ', '+arr[i][1] + '\t' + str(arr[i][2]))

