#!/usr/bin/env python

import os
import sys
import re
from collections import defaultdict

tail = open('tail.bf').read()
t = re.sub(r'[^]+><.[-]', '', tail)
tbl = {'+':1, '<': 2, '>': 3, '-':4, '[':5, ']':6, '.':7}

with open('quine.bf', 'w') as f:
    f.write(">>>>\n\n")
    f.write('>'.join(['+' * tbl[c] for c in t]) + '>' + "\n\n")
    f.write(tail)

d = defaultdict(lambda: 0)
for c in t:
    d[c] += 1

for k,v in sorted(d.items(), key=lambda p:p[1], reverse=True):
    print " %s  %s" % (k, v)
