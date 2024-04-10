# Requirements
# 1 : Prompt user whether to continue
# 2 : Get input from the user
# 3 : Check whether the input is (Y/N)
# 4 : Re run program if 'Y' else quit program if 'N'
# 5 : If the user input is neither 'Y' nor 'N' then print error msg
# 6 : Prompt user again for an input

def get_char():
    y_n = input('Continue?(Y/N):  ')
    return y_n

def convert_char(char):
    if(char == ('Y' or 'y')):
        return 1
    elif(char == ('N' or 'n')):
        return 0
    else:
        return -1

def catch_error(value):
    if(value == -1):
        print('Invalid input!')
        return 1
    else:
        return 0

def prompt_user():
    toll = 1
    while(toll == 1):
        user_input = convert_char(get_char())
        check = catch_error(user_input)