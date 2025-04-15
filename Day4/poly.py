import numpy
from numpy import poly 
from numpy import polynomial 
seq1 = (1,2,3)
seq2 = (1,0,1,1,2,3) 
a = numpy.poly(seq1)  
b = poly(seq2)
print(a,b,"\n")
c = numpy.poly1d(seq1) + numpy.poly1d(seq2)
print(c) #Poly ( 1,0,1, 2,4,6)
