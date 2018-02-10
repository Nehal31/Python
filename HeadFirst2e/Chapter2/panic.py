"""
This module describe about list- '[]' and its operations
li = list() or [] creates the empty list object named li 

make 'Don't Panic' to 'on top' using list operation
using basic list operation pop() and insert we change 
immutable string 'Don't Panic' to 'on top'
"""
#string Don't panic 
phrase = "Don't panic"

#create list plist 
plist = list(phrase)
print(plist)
print(phrase)

#pop() operation to pop out the element of given position
#insert(i,k) insert the value 'k' at given posotion 'i'
plist.pop(0)
plist.pop(2)
plist.insert(3,plist[0])
plist.insert(2,' ')
plist.pop(5)

#create a new string 
new_phrase = ''.join(plist)[0:6]
print(new_phrase)
print(plist)
