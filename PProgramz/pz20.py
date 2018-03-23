''' function to check number is divisible number in a list using  lambda function '''

import random

#take the diviser
d = int(input('Enter the number : '))

#generate the list of 10 random numbers
num_list = [random.randint(2,100) for i in range(1,20) ]

#function to test the divisibilty
div_list = list(filter(lambda x : x % d == 0, num_list ))

print(num_list)
print(div_list)




