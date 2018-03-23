''' take three side of trangle and print its area '''

s1 = float(input('Ent2er first sides of triangle : '))
s2 = float(input('Enter second side of triangle : '))
s3 = float(input('Enter thirs side of the triangle : '))

s = (s1 + s2 + s3 ) / 2
a = (s*(s-s1)+s*(s-s2)+s*(s-s3))**.5

print('Area of the triangle = :', a)
