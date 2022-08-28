from pylab import *
import math
import sympy as sy
x = sy.Symbol('x')

def b(x):
    return 79312*x**6 - 237927*x**5 + 285620*x**4 - 182124*x**3 + 73700*x**2 - 20218*x - 23801
def r(x):
    return 79321*x**6 - 237972*x**5 + 285695*x**4 - 173189*x**3 + 54214*x**2 - 3488*x - 27985
def l(x):
    return 79323*x**6 - 237971*x**5 + 285686*x**4 - 175078*x**3 + 64876*x**2 - 15322*x - 26506

def bprime(x):
    return sy.diff(b(x))
def rprime(x):
    return sy.diff(r(x))
def lprime(x):
    return sy.diff(l(x))

#a,b,c,d is X_Sn in common tangent line
#Rhombo and Liquid phase 사이의 common tangent line
for a in np.arange(0.001,0.2,0.005):
    for b in np.arange(0.2,0.4,0.005):
        if rprime(a) == lprime(b):
            r_tangent = rprime(a)*x -rprime(a)*a +r(a)
            if round(r_tangent.subs(x,b),0) == round(l(b),0):
                #print(r_tangent.subs(x,b),l(b))
                print(a,b)

for c in np.arange(0.6,0.72,0.0003):
    for d in np.arange(0.95,1,0.0003):
        if lprime(c) == bprime(d):
            l_tangent = lprime(c)*x -lprime(c)*c +r(c)
            if round(l_tangent.subs(x,d),1) == round(l(d),1):
                #print(l_tangent.subs(x,d),l(d))
                print(c,d)
