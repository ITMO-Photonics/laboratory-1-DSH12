import scipy
from scipy import linalg
import numpy

A = numpy.zeros((101,101))
i,j = numpy.indices(A.shape)
for k in range (3):
	A[i==j+k]=1
	
B = numpy.zeros((101))
for k in range (101):
	B[k]=k

print (A)
print (B)

x = linalg.solve(A, B)
print(x)
