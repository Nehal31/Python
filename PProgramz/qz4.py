def test(x):
	'''Test the parameter of function'''
	print('x={0} id={1}'.format(x,id(x)))
	x[1]=32 
	print('x={0} id={1}'.format(x,id(x)))

x = [1,3,5,6]
y = (1,2,3,4,)

test(x)
test(x)
test("Hello")
