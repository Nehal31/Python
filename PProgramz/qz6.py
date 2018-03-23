from timeit import Timer

def memoize(fun):
	memo = {}
	def memo_fun(x):
		if x not in memo:
			memo[x] = fun(x)
		return memo[x]
	return memo_fun
@memoize
def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else :
		return(fib(n-1)+fib(n-2))
t = Timer("fib("+str(20)+")","from qz6 import fib")
time = t.timeit(1)
print("%8.7f"%time)
#print(fib(29))
