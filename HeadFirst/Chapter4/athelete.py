"""
this moule is taking input as text file and displaying the sanatized result
'with open' is used to open a file and store is refrence in its object
'split(pantuation)' id used to split the String into two parts when it findes pantuation
'sorted(arg)is a out of place soting function so it required more space '
"""

def sanatize(item):
    if '-' in  item:
        spliter = '-'
    elif ':' in item:
        spliter = ':'
    else:
        return(time)
    (minut,second) = item.split(spliter)
    return(minut+'.'+second)  

with open('james.txt') as file:
    data = file.readline()
james = data.strip().split(',')

with open('julie.txt') as file:
    data = file.readline()
julie = data.strip().split(',')

with open('mikey.txt') as file:
    data = file.readline()
mikey = data.strip().split(',')

with open('sarah.txt') as file:
    data = file.readline()
sarah = data.strip().split(',')


james_arr = []
julie_arr = []
mikey_arr = []
sarah_arr = []

for time in james:
    james_arr.append(sanatize(time))
for time in julie:
    julie_arr.append(sanatize(time))
for time in mikey:
    mikey_arr.append(sanatize(time))
for time in sarah:
    sarah_arr.append(sanatize(time))
    
print(sorted(james_arr))
print(sorted(julie_arr))
print(sorted(mikey_arr))
print(sorted(sarah_arr))
