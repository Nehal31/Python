def mulr(n):
	if n == 1:
		return 3
	else:
		return 3+mulr(n-1)

def sumr(n):
	if n == 0 :
		return 0
	else:
		return n + sumr(n-1)

def pascal_tri(n):
	if n == 1 :
		return [1]
	else:
		prev = pascal_tri(n-1)
		line = [prev[i]+prev[i+1] for i in range(len(prev)-1)]
		line.insert(0,1)
		line.append(1)
	return line


print(mulr(5))
print(sumr(5))
print(pascal_tri(6))
