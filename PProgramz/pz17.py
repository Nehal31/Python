''' display the fibonacci Series   '''
          
#take the test numbers
s = int(input('Enter the maximum steps  : '))


#display the fibonacci series
a = 0
b = 1
print(a , b ,end = ' ')
for i in range(1,s-1):
    c = a + b
    a = b
    b = c
    print(c , end =' ')




