''' display the multiplication table of  given number  '''

import time


           
#take the test numbers
n = int(input('Enter the Number  : '))

#display the multiplication table
for i in range(1,11):
    #print(n ,' * ',i,' = ', n*i )
    print('{0} * {1} = {2}'.format(n,i,n*i))







