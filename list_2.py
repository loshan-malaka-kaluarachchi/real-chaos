def gen_seq(start:int, stop:int, step:int = 1) -> list:
    '''
    Generate a linear sequence
    '''
    seq = []    #Create an empty list
    count = start
    
    while count <= stop:    #Fill list
        seq.append(count)
        count += step
    return seq

def pat_symb(value:int, char:str = '-') -> None:
    '''
    Print a set of characters
    '''
    print(value*char)

def test_parabola():
    x = range(13)
    y = []
    for num in x:
        y.append((num - 6)**2 + 1)

        print(x,'\n',y,sep='')

    for element in y:
        pat_symb(element,'*')