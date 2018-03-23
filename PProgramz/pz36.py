''' set operations - union, intersection, diffrence  '''

#set 1
set1 = set((1,2,4,8,16,32))


#set 2
set2 = set((2,4,8,10,12,14))

#set operations -union
set3 = set1.union(set2)

#set operations -intersection
set4 = set1.intersection(set2)

#set operations -setdifference
set5 = set1.difference(set2)

#set operations -symmetric_difference
set5 = set1.symmetric_difference(set2)

def print_set(my_set,msg = None):
    if msg != None:
        print('Set Operation -',msg ,':')
    for item in my_set:
        print(item, end=' ')

print(set1)
print(set2)
print(set3,'Union')
print(set4,'Intersection')
print(set5,'Set Difference')
print(set6,'Symmetric Difference')
