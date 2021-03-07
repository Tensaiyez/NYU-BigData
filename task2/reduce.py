#!/usr/bin/env python

import sys

count=0
curkey=None
for line in sys.stdin:

	line=line.strip()
	key,value=line.split('\t')

	if curkey==key:
		count+=1

	else:
		if curkey:
			print(curkey + '\t' + str(count))


		curkey=key
		count=1
if curkey==key:
	 print(curkey + '\t' + str(count))

