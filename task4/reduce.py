#!/usr/bin/env python

import sys
import string

curkey=None
count=0



for line in sys.stdin:
	line=line.strip()
	key,value=line.split('\t')
	if curkey==key:
		count=count+1
	else:
		if curkey:
			print (curkey + '\t' +str(count))
		count=1
		curkey=key
		
if curkey==key:
	print (curkey + '\t' +str(count))
