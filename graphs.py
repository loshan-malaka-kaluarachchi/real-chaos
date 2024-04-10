import matplotlib as mpl
import matplotlib.pyplot as pyplt
import numpy as np
from cycler import cycler

def chcksz(lst_1: list, lst_2: list) -> (bool | int):
    ''' Checks size of two lists
        Returns True if sizes are equal else return the difference
    '''
    diff = lst_1.__len__() - lst_2.__len__()
    if diff == 0:
        return True
    else: 
        return diff

def sequence(start: int, stop: int) -> None:
    for value in range(start,stop):
        ind_var.append(value)

        
ind_var = []
dep_var = []

sequence(0,9)

for value in ind_var:
    dep_var.append(2*value)

pyplt.figure()    
fig = pyplt.subplot()
fig.stem(dep_var,markerfmt='o',)
pyplt.xlabel('$x$')
pyplt.ylabel('$y$')
pyplt.grid(visible=True,which='both')
pyplt.show()
