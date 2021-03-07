#!/usr/bin/env python

import sys
import string
import csv

data=csv.reader(sys.stdin,delimiter=',')

for info in data:    
    if len(info) == 22:
        print(info[0] + '\t' + info[14] + ', ' + info[6] + ', ' + info[2] + ', ' + info[1])
    elif len(info) == 18:
        print(info[0] + '\t' + '***')

