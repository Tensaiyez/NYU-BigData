#!/usr/bin/env python

import sys
import string

liscense = None
count = 0
valTotal = 0.0

for line in sys.stdin:

	line = line.strip()
	key, amt= line.split('\t', 1)
   
	tot, num = amt.split(',', 1)
	tot = float(tot)

	if key == liscense:
		count += 1
		valTotal += tot
	elif liscense:
		print("{0:s}\t{1:.2f}, {2:.2f}".format(liscense, valTotal, valTotal/count))
		valTotal  =tot
		liscense = key
		count=1
  	else:
		valTotal  =tot
                liscense = key
                count=1


if liscense == key:

	print("{0:s}\t{1:.2f}, {2:.2f}".format(liscense, valTotal, valTotal/count))
