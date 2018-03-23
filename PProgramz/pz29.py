''' Decimal to binary conversion using recursion  '''

#Decimal to binary conversion recursive function
def dec_to_bin(n):
    if n > 1:
        dec_to_bin(n//2)
    print(n % 2,end = ' ')

#take the steps
d = int(input('Enter the Decimal Number  : '))

print('Binay number of Decimal Number {0} is :  '.format(d))
dec_to_bin(d)

