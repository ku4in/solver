#!/usr/bin/env python3

import sys
from sympy import *
import string
import re

MATH =  [
        'abs' , 'sqrt', 'cbrt', 'root',
        'log' , 'ln'  , 'exp' ,
        'pi'  , 'sin' , 'cos' , 'tan' , 'cot' , 'sec' , 'csc', 'sinc',
        'asin', 'acos', 'atan', 'acot', 'asec', 'acsc', 'atan2',
        'sinh', 'cosh', 'tanh', 'coth', 'sech', 'csch',
        'asinh','acosh','atanh','acoth','asech','acsch',
        ]

if len(sys.argv) > 1:
    fname = sys.argv[1]
    fil = open(fname, 'r')
else:
    fname = ''
    fil = sys.stdin

# Set the names of the variables: a = 'a', b = 'b', etc.
for ch in string.ascii_lowercase:
    globals()[ch] = symbols(ch)

system = []
while ss:= fil.readline():
    if ss != '\n':
        ss  = ss.split('\n')[0]
        if fname: print(ss)
        # Excluding math function of subsequent processing by replacing them with <n> mark,
        # where <n> is the number of function in MATH list
        dic = {}
        for ii, mm in enumerate(MATH):
            mat = None
            mat = re.search(mm, ss)
            if mat: 
                dic[ii] = mat.group()
                ss = re.sub(mm, f"<{ii}>", ss)

        # Add '*' between variables and numbers: 10xy --> 10*x*y
        ss = re.sub('([a-z0-9)])(?=[a-z<(])', r'\1*', ss)
        # Return math functions back
        for ii, mm in dic.items():
            ss = re.sub(f"<{ii}>", f"{mm}", ss)
        eq = ss.split('=')
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

fil.close()
