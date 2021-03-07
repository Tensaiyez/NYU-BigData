#!/usr/bin/env python

import sys
import string


curkey = None
infoval = None
num = 0

for line in sys.stdin:
	line = line.strip()
	summons,info = line.split('\t', 1)
    
	if curkey == summons:
		num=num+1	
	else:
		if curkey and num==1 and infoval!='***':	
			print(curkey + '\t' + infoval)
		curkey = summons
		num = 1
		infoval = info
if num ==1:
	if info != '***':
		print(summons + '\t' + info)
