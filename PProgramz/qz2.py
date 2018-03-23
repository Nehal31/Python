from qz1 import fibr,fibi
from timeit import Timer

#t1 = Timer("fibr(30)","from qz1 import fibr")
#print(t1.timeit(3))
for i in range(1,255):
	s = "fibr(" + str(i) + ")"
	t1 = Timer(s,"from qz1 import fibr")
	time1 = t1.timeit(3)
	s = "fibi(" + str(i) + ")"
	t2 = Timer(s,"from qz1 import fibi")
	time2 = t2.timeit(3)
	s = "fibm(" + str(i) + ") "
	t3 = Timer(s,"from qz1 import fibm")
	time3 =  t3.timeit(3)
	print("n = %2d, fibr:%8.6f, fibi:%8.6f,fibm:%8.6f percent : %10.2f"%(i, time1,time2,time3,time1/time2))


