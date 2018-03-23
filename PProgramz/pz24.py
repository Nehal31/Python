''' calculate the Factor of the numbers '''

#take the inputs
n = int(input('Enter any  Number : '))


#calculate the Factor of the number
def factor(b):
    fac = []
    for i in range(1,int(n/2)+1):
        if (n % i == 0):
            fac.append(i)
    return fac



print('Factor(s) of {0} is/are : {1}'.format(n,factor(n)))

