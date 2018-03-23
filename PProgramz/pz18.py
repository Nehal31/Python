''' print the armstrong numbers in the given range   '''

        
#fun for checking the armstrong number
def armstrong(num):
    arm = num
    lent = len(str(num))
    summ = 0
    while(num > 0):
        summ += (num%10)**lent
        num = int(num/10)
               
    if arm == summ :
        return True
    else :
        return False
          
#take the test numbers
l = int(input('Enter the lower bond : '))
u = int(input('Enter the upper bond : '))

#print the arstrong number of given range
for i in range(l,u+1):
    if armstrong(i):
        print(i ,end = ' ')
    



