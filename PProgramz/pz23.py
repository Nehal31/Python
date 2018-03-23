''' calculate the GCD of given two numbers '''

#take the inputs
x = int(input('Enter any first Number : '))
y = int(input('Enter the secont Number :'))

#calculate the GCD using uclidian method
def gcd(a,b):
    while(b):
        a,b = b,a % b
    return a


print('GCD of {0} and {1} is : {2}'.format(x,y,gcd(x,y)))

