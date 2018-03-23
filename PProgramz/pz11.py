''' check the given year is leap or not '''

#taking the given year
y = int(input('Enter the year : '))

#check the Leap year
if y % 4 == 0:
    if y % 100 == 0:
        if y % 400 == 0 :
            print('Leap Year')
        else:
            print('Not leap Number')
    else :
        print('Leap year ')
else:
    print('Not leap Year')




