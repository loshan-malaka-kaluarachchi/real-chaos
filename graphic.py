def border(start:str, middle: str, repeats: int) -> None:
    ''' Prints a list of characters'''
    sample = start + ' ' + 3*middle + ' '
    border = sample*repeats + start
    print(border)

for index in range(1,6):
    border('+','-',index)
    
for index in range(6,0,-1):
    border('+','-',index)
