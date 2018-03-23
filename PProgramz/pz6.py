''' Generate and Print Random Number '''

import random

l = int(input('Enter the lower value of random number : '))
u = int(input('Enter the upper value of random number : '))

#random number 
r = random.randint(l,u)

print('Generated Random number',r)

