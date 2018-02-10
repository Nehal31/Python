''' this code show the use of dictionay to count
 the frequency of vowels in given string  
'''


vowels = ['a','e','i','o','u']
find = {}

value = input("Enter the String")
for each_char in value:
    if each_char in vowels:
        if each_char not in find:
            find[each_char] = 0
        find[each_char] += 1
    
for k,v in sorted(find.items()):
    print(k ,"has the frequency ",v)

