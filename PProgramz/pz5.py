''' Swap two varivale using temp variable '''
''' Swap two varivale without using temp variable '''

a = input('Enter the value of a : ')
b = input('Enter the value of b : ')

print('Given value of a = {0} and b ={1}'.format(a,b))

#swap using temp variable:
t = a
a = b
b = t
print('swap using temp variable:')
print('Changed value of a = {0} and b ={1}'.format(a,b))

#swap without temp variable:
print('swaping without temp variable:')
a,b = b,a

print('Changed value of a = {0} and b ={1}  '.format(a,b))
