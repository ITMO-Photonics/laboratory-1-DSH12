import scipy
from scipy import linalg
import numpy as np
import time

N=100
A = np.random.random((N,N))
#print(A)

B = np.zeros((N))
def b_k(k, t):
    return (k/(1.+k*t))

time_start = time.process_time()
t=0.
while t<=10.:
	for k in range (N):
		B[k]=b_k(k,t)
	x = linalg.solve(A, B)
	xnorm = linalg.norm(x)
	#print(xnorm)
	t=t+0.1
print("linalg.solve time =", time.process_time()-time_start)

time_start = time.process_time()
t=0.
PLU= linalg.lu_factor(A)
while t<=10.:
	for k in range (N):
		B[k]=b_k(k,t)
	x = linalg.lu_solve(PLU, B)
	xnorm = linalg.norm(x)
	#print(xnorm)
	t=t+0.1
print("linalg.lu_solve time =", time.process_time()-time_start)

time_start = time.process_time()
Ainv=linalg.inv(A)
t=0.
while t<=10.:
	for k in range (N):
		B[k]=b_k(k,t)
	x = np.dot(Ainv, B)
	xnorm = linalg.norm(x)
	#print(xnorm)
	t=t+0.1
print("linalg.inv time =", time.process_time()-time_start)
