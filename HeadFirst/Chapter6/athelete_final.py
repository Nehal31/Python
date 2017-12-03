"""
this moule is taking input as text file and displaying the sanatized result
'with open' is used to open a file and store is refrence in its object
'split(pantuation)' id used to split the String into two parts when it findes pantuation
'sorted(arg)is a out of place soting function so it required more space '
'Dictionary' A built-in data structure (included with Python) that allows you-
to associate data with keys, as opposed to numbers. This lets your in-memory-
data closely match the structure of your actual data.
"""

def sanatize(item):
    if '-' in  item:
        spliter = '-'
    elif ':' in item:
        spliter = ':'
    else:
        return(item)
    (minut,second) = item.split(spliter)
    return(minut+'.'+second)  

def get_data(file_name):
    try:
        with open(file_name) as file:
            temp = file.readline()
        data = temp.strip().split(',')
        return ({'name' : data.pop(0),
                'dob' : data.pop(0),
                'time' : str(sorted(set([sanatize(time) for time in data]))[0:3])})
    except IOError as ioarr:
        print ("IOError :"+str(ioarr))
        return(None) 
james = get_data('james.txt')
julie = get_data('julie.txt')
mikey = get_data('mikey.txt')
sarah = get_data('sarah.txt')

# Store the list items in sets to remove the duplicate items
# Print the frist least three times if stored set

print(james['name'] + "'s firstest timeings are " +james['time'])
print(julie['name'] + "'s firstest timeings are " +james['time'])
print(mikey['name'] + "'s firstest timeings are " +james['time'])
print(sarah['name'] + "'s firstest timeings are " +james['time'])
