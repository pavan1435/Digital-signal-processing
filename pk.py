#code on linear algebraic operations
import numpy as np
a=input("enter matrix1:")
b=input("enter matrix2:")
m1=np.array(a)
m2=np.array(b)
#operations on two matrices
print "operations of linear algebra by using numpy"
print "addition of two matrices--\n",np.add(m1,m2)
print "subtraction of two matrices--\n",np.subtract(m1,m2)
print "multiplication of two matrices--\n",np.dot(m1,m2)
print "division of two matrices--\n",np.divide(m1,m2)
print "linear solution is--\n",np.linalg.solve(m1,m2)
#operations on 1 matrix
print "transpose of matrix1--\n",np.transpose(m1)
print "trace of matrix1--\n",np.trace(m1)
print "determinant of matrix1--\n",np.linalg.det(m1)
print "rank of matrix1--\n",np.linalg.matrix_rank(m1)
print "maximum value in matrix1--\n",np.max(m1)
print "minimum value in matrix1--\n",np.min(m1)
print "power of matrix1--\n",np.linalg.matrix_power(m1,3)
print "eigen values of matrix1--\n",np.linalg.eig(m1)


