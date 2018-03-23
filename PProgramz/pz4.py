''' Find the roots of the quadratic equation '''

import cmath

print('quadratic equation - aX^2 + bx + c')
a = float(input('Enter the value of a : '))
b = float(input('Enter the value of b : '))
c = float(input('Enter the value of c : '))

#calculate the discrimant
d = b**2 - (4*a*c)

#first root
x1 = (-b + cmath.sqrt(d))/(2*a)
x2 = (-b - cmath.sqrt(d))/(2*a)


print('First root :', x1 , 'Second Root',x2)
