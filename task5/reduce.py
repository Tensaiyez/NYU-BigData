#!/usr/bin/env python

import sys
import string

curkey=None
buff={}
num=0

for line in sys.stdin:
        line=line.strip()

        key,value=line.split('\t',1)
        if key ==curkey:
		num+=1
	elif curkey:
		buff[curkey]=num
                curkey=key
                num=1
	else:
		curkey=key
		num=1
if key==curkey:
	buff[curkey]=num
sortInfo=sorted(buff.items(),key=lambda x: x[1], reverse=True)

print ("{0}\t{1}".format(sortInfo[0][0],sortInfo[0][1]))

