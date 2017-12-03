"""
this moule is taking input as text file and displaying the sanatized result
'with open' is used to open a file and store is refrence in its object
'split(pantuation)' id used to split the String into two parts when it findes pantuation
'sorted(arg)is a out of place soting function so it required more space '
'Dictionary' A built-in data structure (included with Python) that allows you-
to associate data with keys, as opposed to numbers. This lets your in-memory-
data closely match the structure of your actual data.
"""

class Athelete:
    def __init__(self,name,dob=None,time=[]):
        self.name = name
        self.dob = dob
        self.time = time

    def top3(self):
        def sanatize(item):
            if '-' in  item:
                spliter = '-'
            elif ':' in item:
                spliter = ':'
            else:
                return(item)
            (minut,second) = item.split(spliter)
            return(minut+'.'+second)
        return(str(sorted(set([sanatize(time) for time in self.time]))[0:3]))

    def add_time(self,time):
        self.time.append(time)

    def add_times(self,times):
        self.time.extend(times) 

def get_data(file_name):
    try:
        with open(file_name) as file:
            temp = file.readline()
        data = temp.strip().split(',')
        return (Athelete(data.pop(0),data.pop(0),data))
    except IOError as ioarr:
        print ("IOError :"+str(ioarr))
        return(None) 
james = get_data('james.txt')
julie = get_data('julie.txt')
mikey = get_data('mikey.txt')
sarah = get_data('sarah.txt')

# Store the list items in sets to remove the duplicate items
# Print the frist least three times if stored set

print(james.name + "'s firstest timeings are " + james.top3())
print(julie.name + "'s firstest timeings are " + julie.top3())
print(mikey.name + "'s firstest timeings are " + mikey.top3())
print(sarah.name + "'s firstest timeings are " + sarah.top3())
