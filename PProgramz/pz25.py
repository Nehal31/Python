''' Calculator Program  '''

#take the inputs
a = int(input('Enter first  Number : '))
b = int(input('Enter second Number : '))


def select_menu():
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('!!!#======================#!!!')
    print('!!!#    CALCULATOR MENU   #!!!')
    print('!!!#======================#!!!')
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('!!!************************!!!')
    print('!!! 1 - Addition           !!!')
    print('!!! 2 - Substration        !!!')
    print('!!! 3 - Multiplication     !!!')
    print('!!! 4 - Division           !!!')
    print('!!! 5 - Quit               !!!')
    print('!!!************************!!!')
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('!!!~~~~~~~~~~~~~~~~~~~~~~~~!!!')
    print('!!!Select :-               !!!')
    print('!!!~~~~~~~~~~~~~~~~~~~~~~~~!!!')
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')


select_menu()
c = input()

def out(c):
    if c == '1' :
        return a + b
    elif  c == '2' :
        return a - b
    elif c == '3' :
        return a * b
    elif c == '4' :
        return a / b
    else:
        quit()

print('Your Answer is :',out(c))

