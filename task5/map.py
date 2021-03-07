#!/usr/bin/env python

import csv
import sys
import string

data=csv.reader(sys.stdin,delimiter=',')

for info in data:
        print(info[14] + ', ' +info[16] + '\t' + '1')


