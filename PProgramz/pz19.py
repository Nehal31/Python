''' sum of the numbers  '''

        
#fun for calculte sum up to the number
def natural_sum(num):
    return num * (num + 1 ) / 2
         
#take the test numbers
n = int(input('Enter the number : '))

ns = natural_sum(n)

#print the sum of natural number up to the number
print('sum of natural number up to the number {0} is :{1}'.format(n,ns))

