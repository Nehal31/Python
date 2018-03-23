''' print the fibonacci using recursion  '''

#fibonacci recusive function
def fibo_rec(n):
    if n <= 1:
        return n
    else :
        return (fibo_rec(n-1)+fibo_rec(n-2))

#take the steps
s = int(input('Enter the steps : '))

for i in range(s):
    print(fibo_rec(i),end = ' ')




