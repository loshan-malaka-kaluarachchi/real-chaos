#Creating the fibonacci sequence
list_len = 15
a = [0,1]
rat_a = []
num = 0

print('Creating the fibonacci sequence:')
print(list_len*'-')

for i in range(0,list_len + 1):
    num = a[i] + a[i + 1]
    a.append(num)
        
print(a)
print('No of items in list:',len(a))
print('\n')

for i in range(0,list_len + 1):
    ratio = a[i]/a[i + 1] + 1
    rat_a.append(ratio)
    print(i + 1,'--',ratio)
    