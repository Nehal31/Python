''' soth the world in alphabatic order '''

#take the string input
str_val = input('Enter your String :')

#split into words
str_list = str_val.strip().split(' ')

#sort the words
str_list.sort()

#print the sorted word list
for word in str_list:
    print(word)
