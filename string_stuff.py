verbose = r"""

fname = 'Sparks'
age = 12
sender = 'Mark'
subject = 'New Message'
title = 'Subject:{0}'.format(subject)
line = '-'*50
pattern = f'''
Dear {fname},

Happy Birthday!
You are {age} years old.
Thanks.

Sincerely
{sender}
'''
print(line)
print(title)
print(line)
print(pattern)
print(line)

"""
fname = 'Sparks'
age = 12
sender = 'Mark'
subject = 'New Message'
title = 'Subject:{0}'.format(subject)
line = '-'*50
pattern = f'''
Dear {fname},

Happy Birthday!
You are {age} years old.
Thanks.

Sincerely
{sender}
'''
print(line)
print(title)
print(line)
print(pattern)
print(line)
print(verbose)