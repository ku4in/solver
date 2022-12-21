# solver
Simple python script to solve equations and systems of equations

**Usage:** solver.py [data]

_`data` is a file containing equations and systems of equations (each equation on a new line) separated by at least one blank line. All lowercase characters a..z are treated as variables. If `data` file is not specified then solver.py reads standard input. In this case it does not print equations themselves before solutions, so this can be used as an interactive mode. `*` symbol can be omitted, i.e. `xyz` will be treated as x\*y\*z or you can simply type like this: 3(x + 1)(y - 2). But math functions are recognized by parser and will remain as they are, i.e. you can use abs(x) or sin(x + pi/4)_
    
