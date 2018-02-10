'''

'''
def match_value(phrase:str, letters:str = 'aeiou')->str:
    return set(phrase).intersection(set(letters))
