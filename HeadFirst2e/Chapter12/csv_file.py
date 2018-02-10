
file_loc = 'test1.csv'

def time_formate(val):
    k,t = val.split(':')
    p = int(k)
    if p >12:
        k = p - (p - 12)
        k = str(k)+':'+t
        i = k +' P.M'
    else:
        i = k +':'+t+' A.M'

    return i

def value_formate(msg):
    return msg.title()

with open(file_loc) as file:
    head_ignore = file.readline()
    flights = {}
    for line in file:
        k,v = line.strip().split(',')
        k = time_formate(k)
        v = value_formate(v)
        flights[k] = v

