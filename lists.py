'''
values = [1,2,3,4,5,6,]
print(values)
var = ''
print(var)
for num in values:
    txt = bin(num).removeprefix('0b')
    last_bit = txt[-1]
    var = var.__add__(last_bit)
    print(num,txt)
    
print(int(var,base=2),var)
values.append((int(var,base=2)))

print(values)
'''
#---------------------------------------------#
#Exercise 2
#Expected Output: [2,4,6,8]

def remove_repeats(origin:list) -> list:
    """Implement methods of <class 'list'> to remove re-occuring values 

    Args:
        set (list): 

    Returns:
        list: Modified set
    """    
    set = origin.copy()
    set.sort()
    for value in set:
        while set.count(value) > 1:
            set.remove(value)
    return set
 
 
numList = [1,5,7,9,6,6,3,5,7,8,1,4,2,6,7,9,3]
new = remove_repeats(numList)
print(numList,'\n',new,sep='')


#---------------------------------------------#

'''
count = 1
for i in range(1,11):
    for j in range(1,10):
        if str(count).__len__() == 1:
            print(count,end='  | ')
        else:
            print(count,end=' | ',sep="")
        count += 1
    print('\n')
'''
