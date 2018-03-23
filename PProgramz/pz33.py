''' Remove the pantuation from the string '''

#Puntuations
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

str_val = input('Enter your String :')

#function for remove pentuation 
def rmv_pan(str_val):
    new_str = ""
    for char in str_val:
        if char not in punctuations:
            new_str = new_str + char
    return new_str

print('Modified String  : ',rmv_pan(str_val))
