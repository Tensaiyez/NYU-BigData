#!/usr/bin/env python

import sys
import csv

data=csv.reader(sys.stdin, delimiter=',')

for info in data:

   	if info[12]:
		value=float(info[12])
	else:
		value=float(0.00)
	
	print(info[2] + '\t'+str(value)+',' + '1.00')
