"""
Athelete is the subclass which inherit the base class list
__init__ method is the very first function of ezch class so much be declared for each class
'self' is the first argument and it the repaced by the object refrence
Athelete class has all the feature of list class
'list.append' is add new list
list.extend' is add new element to the list
"""

class Athelete(list):
    def __init__(self,name,dob=None,time=[]):
        list.__init__([])
        self.name = name
        self.dob = dob
        self.extend(time)

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
        return(str(sorted(set([sanatize(time) for time in self]))[0:3]))

    
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
