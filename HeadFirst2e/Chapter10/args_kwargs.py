
def myfun1(*args)->list:
    for item in args:
        print(item, end=' ')
    if args:
        print()

def myfun2(**kwargs)->dict:
    for key,value in kwargs:
        print(key,'->',value, end=' ')
    if kwargs:
        print()

def myfun3(*args, **kwargs ):
    if args:
        for item in args:
            print(item, end = ' ')
        print()

    if kwargs:
        for key,value in kwargs:
            print(key, '->', value, end = ' ')
        print()
