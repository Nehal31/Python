"""
This code repeatedly check the time at random time interval

'datetime' module contains 'datetime' submodule which gives today's time 
using 'today()' built in function 

'random' module contains 'randrange(int)' function which return a random 
integer of that range excluding last number 
  
'time module' provides 'sleep()' funtion whose parameter are seconds
"""

from datetime import datetime
import random
import time

odds = [i for i in range(1,60,2)]
for i in range(10):
    current_minutes = datetime.today().minute
    if current_minutes in odds:
        print("Minutes are odd")
    else :
        print("Minutes are not odd")

    # random number generation
    rand_int = random.randint(1,60)
    time.sleep(rand_int)



