''' factorial of given number  '''

import time


#calculate factorial recursively
def fact_rec(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fact_rec(n-1)

#calculate factorial itteratively
def fact_ite(n):
    fact = 1
    for i in range(1,n+1):
        fact *=i
    return fact

           
#take the test numbers
n = int(input('Enter the Number  : '))

#recursive performance
print('recursive performance :')
start_time =  time.time()     
print(fact_rec(n))
print(time.time() - start_time )

#itterative performance
print('itterative performance')
start_time =  time.time()     
print(fact_ite(n))
print(time.time() - start_time )






