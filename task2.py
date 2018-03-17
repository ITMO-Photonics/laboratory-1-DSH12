import scipy
from scipy import optimize
import numpy

import time

def f(x):
	return (numpy.cos(x))/(1.+x*x)

def f1(x):
	return (-(numpy.sin(x))/(1.+x*x))-((2.*x*numpy.cos(x))/((1.+x*x)*(1.+x*x)))
	
t = time.process_time()
for i in range (10000):
	sol = optimize.bisect(f, 0.1, 2.4)
print("bisect result =", sol, "t =", (time.process_time()-t))
t = time.process_time()
for i in range (10000):
	sol = optimize.newton(f, 1., f1)
print("newton and f1 result =", sol, "t =", (time.process_time()-t))
t = time.process_time()
for i in range (10000):
	sol = optimize.newton(f, 1.5)
print("newton result =", sol, "t =", (time.process_time()-t))
t = time.process_time()
for i in range (10000):
	sol = optimize.brentq(f, 0.1, 2.4)
print("brentq result =", sol, "t =", (time.process_time()-t))
