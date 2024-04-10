#Even odd number checker
number = float(input("Enter value: "))

if number == 0:
    print('Value is zero!')
elif number%2 == 0:
    print('The number you entered is even.')
    
elif number%2 == 1:
    print('This number you entered is odd')
