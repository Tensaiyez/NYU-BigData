#!/usr/bin/env python
import sys
import csv
import string

for line in sys.stdin:
	line = line.strip()
	row=csv.reader([line],delimiter=',')
	row=list(row)[0]
	cd=row[2]
	date=row[1]
	year,month,day=date.split('-',2)
	weekend=(5,6,12,13,19,20,26,27)
	if int(day) in weekend:
		print(cd+'\t'+ '1.00')
