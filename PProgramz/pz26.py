''' suffle the deck of cards  '''

import itertools
import random

#list of all the numbers
a = [i for i in range(1,14)]

#list of all the types
b = ['Dimond','Spread','Heart','Club']

#cartesion product of a and b
deck = list(itertools.product(a,b))

#random shuffle of deck
random.shuffle(deck)

for i in range(0,13):
    print(deck[i][0],' ',deck[i][1])




