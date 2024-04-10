def get_bin(dec_num : int) -> str:
    '''
    Returns a binary string when given an integer
    '''
    return bin(dec_num).removeprefix('0b')

def series_1(seed : int, steps : int) -> None:
    count = 0
    while count < steps:
        print(seed,3*'\t',get_bin(seed))
        seed <<= 1
        seed += 1
        count += 1
    print(seed,3*'\t',get_bin(seed))

def series_2(seed : int, steps : int) -> None:
    count = 0
    while count < steps:
        print(seed,3*'\t',get_bin(seed))
        seed <<= 1
        seed += 1
        count += 1
    print(seed,3*'\t',get_bin(seed))

def show_bin_val(value : int) -> None:
    bin_val = bin(value).removeprefix('0b')
    n_chars = bin_val.__len__()
    ones = value.bit_count()
    zeros = n_chars - ones
    msg = f'''
Value - {value}
Binary - {bin_val}
Zeros - {zeros}
Ones - {ones}
'''
    print(msg)

#################################
'''  
x = 1
y = 2
z = 3

if x > y & x > z:
    print(f'{x} > {y} and {x} > {z}')
    if y > z:
        print(f'{y} > {z}')
        print(f'{x} > {y} > {z}')
    elif y == z:
        print(f'{y} = {z}')
        print(f'{x},{y}={z}')
    else:
        print(f'{y} < {z}')
        print(f'{x} > {z} > {y}')
elif x > y | x > z:
    if x > y:
        print(f'{x} > {y}')
        if x == z:
            print(f'{x} = {z}')
            print(f'{x} = {z} > {y}')
        else:
            print(f'{x} < {z}')
            
'''       
