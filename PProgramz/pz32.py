''' Palindrome Test of string '''

import math
str_val = input('Enter your String :')

str_val = str_val.casefold()

#function for palindrom check
def check_pal(str_val):
    str_len = len(str_val)
    for i in range(math.ceil(str_len/2) ):
        if str_val[i] == str_val[str_len-(i+1)]:
            pass
        else:
            return False
    return True

print('Is String Palindrom : ',check_pal(str_val))
