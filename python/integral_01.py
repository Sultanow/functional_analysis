from sympy import *
from sympy.printing.latex import print_latex

t = Symbol('t')
x = Symbol('x')
a = Symbol('a')
b = Symbol('b')

print_latex(integrate(a*exp(x)/t, (x, 0, oo)))
print_latex(integrate(exp((-a*t**2+I*b*t)/(3*t**2+1)+I*t*x)*(x/(3*t**2+1)), (t, -oo, oo), (x, 0, oo)))