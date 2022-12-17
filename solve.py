#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    print(f"Usage: {sys.argv[0]} file", file=sys.stderr)
    sys.exit(1)

from sympy import *
import string
import re

# set variables names a = 'a', b = 'b', etc.
for ch in string.ascii_lowercase:
    globals()[ch] = symbols(ch)

system = []
with open(fname, 'r') as f:
    while s:= f.readline():
        if s != '\n':
            s  = s.split('\n')[0]
            print(s)
            s = re.sub('(\d+)([^0-9+-/*=\s])', r'\1*\2', s)
            eq = s.split('=')
            system.append(Eq(eval(eq[0]), eval(eq[1])))
        else:
            if system:
                print(solve(system))
                print()
            system = []
    else:
        if system:
            print(solve(system))
            print()
