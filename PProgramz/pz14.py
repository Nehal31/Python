''' print the prime numbers in given interval '''

import time

start_time =  time.time()
#check the prime number
def check_prime1(n):
    i = 2
    if n == i:
        return True
    while True:
        if n % i == 0:
            return False
        if i**2 >= n:
            return True
        i+=1

def check_prime2(num):
    if num == 2:
        return True
    else:
        for i in range(2,num):
            if (num % i) == 0:
               return False
        return True

           
#take the test numbers
l = int(input('Enter the lowest bond : '))
h = int(input('Enter the height bond : '))

pl = []
count = 0 

#print the prime numbers
for i in range(l,h):
    if check_prime2(i):
        pl.append(i)
        count+= 1
        
print(time.time() - start_time )
print(count)
print(pl)
print(time.time() - start_time )






