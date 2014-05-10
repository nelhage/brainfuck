#!/usr/bin/env python

import os
import sys
import re

tail = open('tail.bf').read()
t = re.sub(r'[^]+><.[-]', '', tail)
tbl = {'+':1, '<': 2, '>': 3, '-':4, '[':5, ']':6, '.':7}

with open('quine1.bf', 'w') as f:
    f.write(">>>>\n\n")
    f.write('>>>>'.join(['+' * tbl[c] for c in t]) + '>>>>' + "\n\n")
    f.write(tail)
