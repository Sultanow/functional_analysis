from sympy import *
from sympy.core.numbers import Infinity
from sympy.printing.latex import print_latex

x = Symbol('x')

print_latex(integrate(1/(x**2-sin(x)-1), x))
#print_latex(integrate(exp(-x)*sqrt(cos(x))/(sqrt(cos(x))+sqrt(sin(x))), (x, 0, pi/2)))
#print_latex(integrate(sqrt(x)+x**3, (x, 0, Infinity)))
#print_latex(integrate(x**(x**x), (x, 0, 1)))