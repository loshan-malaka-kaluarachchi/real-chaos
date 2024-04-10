word = 'Some text in a line'
number = 421

print(f'This is an integer:\t\"{number}\"')

my_string = '{0} {1} {2} {3} {4}'.format('Zero', 'One', 'Two','Three','Four')
string  = 3*'{0} {1}{1}{1} '.format('+','-')
print(string + '\n' + my_string)