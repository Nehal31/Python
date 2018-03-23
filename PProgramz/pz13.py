''' check for the prime number '''

#take the test numbers
n = int(input('Enter the number greater than 2 : '))

#check the prime number
i = 2
while(True):
    if n % i == 0:
        print('Not Prime number ')
        break
    if i**2 >= n:
        print('Prime Number')
        break
    i+=1







