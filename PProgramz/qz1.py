def fibr(n):
	if n == 0:
		return 0
	elif n == 1:
 		return 1
	else :
		return(fibr(n-1)+fibr(n-2))

def fibi(n):
	old , new = 0,1
	if n == 0:
		return 0
	else:
		for i in range(n-1):
			old, new = new, new+old
	return new

memo = {0:0, 1:1}	
def fibm(n):
	''' fibm is a recursion function which remember the
		 memory location using the memo distnary'''
	if not n in memo:
		memo[n] = fibm(n-1) + fibm(n-2)
	return memo[n]
