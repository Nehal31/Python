def avg_gen():
	count = 0
	total = 0
	average = None 
	while True:
		term = yield average
		total += term
		count += 1
		average = total / count

ag = avg_gen()
next(ag)

for value in range(1,100000):
	print("Val : {0} average :{1:8.3f} ".format(value,ag.send(value)))
	
