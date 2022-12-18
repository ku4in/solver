#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = ''

from sympy import *
import string
import re

# Set the names of the variables: a = 'a', b = 'b', etc.
for ch in string.ascii_lowercase:
    globals()[ch] = symbols(ch)

if fname:
    f = open(fname, 'r')
else:
    f = sys.stdin

system = []
while s:= f.readline():
    if s != '\n':
        s  = s.split('\n')[0]
        if fname: print(s)
        # Add '*' between variables and numbers: 10xy --> 10*x*y
        s = re.sub('([a-z0-9])(?=[a-z(])', r'\1*', s)
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
