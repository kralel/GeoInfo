from math import *

#Coefficients of quadratic polynomial
a = 6
b = 5
c = 1
#Compute discriminant
D = b**2 - (4*a*c)
#Counting roots x1, x2, if D > 0
if D > 0:
    x1 = (-b + D**(1/2))/(2*a)
    x2 = (-b - sqrt(D))/(2*a)
    print("Two roots, x1", x1, "x2", x2)
#Counting roots x1 = x2, if D == 0
elif D == 0:
    x1 = (-b)/(2*a)
    print("x1=x2", x1)
#Counting roots x1, x2, if D < 0
else:
    print("No solution in R.")