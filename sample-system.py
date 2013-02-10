import numpy

y12 = 15.0
y21 = 13.0

y1 = y21
y2 = y12

e1 = 20.0
e2 = 22.0

b = numpy.array([e2,
                 y21])

A = numpy.matrix([[1, -1],
                  [0,  1]])

ans = numpy.linalg.solve(A, b)
