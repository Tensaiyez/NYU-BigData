#!/usr/bin/env python

import sys
import string
import csv

words=csv.reader(sys.stdin,delimiter=',')

for data in words:
	if data[16]=='NY':
		key=data[16]
	else:
		key= 'Other'
	print(key+ '\t'+ '1')
		
