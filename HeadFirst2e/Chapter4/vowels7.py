'''
the code uses the set() to find the vowels in the input sequence
'''
vowels = set('aeiou')
value = input("Enter the String")
i = vowels.intersection(set(value))
for v in sorted(i):
    print(v)

