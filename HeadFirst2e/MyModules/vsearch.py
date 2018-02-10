"""
:str and ->set are anotation which documented thet the input is str type and return is set type
"""

def fun4vowels(value:str)->set:
    """fun4vowels is a function to find the strings in the given strings  """
    vowels = set('aeiou')
    return vowels.intersection(set(value))

def fun4letters(value:str,letters:str='aeiou')->set:
    return set(letters).intersection(set(value))
