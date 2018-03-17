import scipy
from scipy import optimize
import numpy

def f(x):
	return (numpy.cos(x))/(1+x*x)

def f1(x):
	return ((numpy.sin(x))/(1+x*x))-((2*x*numpy.cos(x))/((1+x*x)*(1+x*x)))
	
sol = optimize.bisect(f, 0.1, 2.4)
sol = optimize.newton(f, 1, f1)
sol = optimize.newton(f, 1.5)
sol = optimize.brentq(f, 0.1, 2.4)
