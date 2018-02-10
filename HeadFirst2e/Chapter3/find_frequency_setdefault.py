'''
This code show the use of setdefault() bif of dict 
setdefault add new key and set the default value 0 
to the key if it doesn't exist
'''

vowels = ['a','e','i','o','u']
find = {}

value = input("Enter the String")
for each_char in value:
    if each_char in vowels:
        find.setdefault(each_char,0)
        find[each_char] += 1
   
for k,v in sorted(find.items()):
    print(k ,"has the frequency ",v)

