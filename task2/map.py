#!/usr/bin/env python

import sys
import csv

data=csv.reader(sys.stdin,delimiter=',')
for info in data:
	
	print(info[2] + '\t' + str(1))
