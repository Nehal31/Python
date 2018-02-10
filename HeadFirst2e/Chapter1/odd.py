'''This is Code which tells current minutes 
is odd or even
'''
#import datetime.datetime class
from datetime import datetime

#list comprehension
odds = [i for i in range(1,60,2)]

#get the minutes
current_minutes = datetime.today().minute

#check current minutes is in odds list
if current_minutes in odds:
    print("Minutes are odd")
else :
    print("Minutes are not odd")
