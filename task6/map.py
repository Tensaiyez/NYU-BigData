#!/usr/bin/env python
import sys
import csv

data=csv.reader(sys.stdin,delimiter=',')

for info in data:
	state=info[16]
	if state=='99' or state.isalpha():
	 	print(info[14] + ', ' +state + '\t' + '1')
