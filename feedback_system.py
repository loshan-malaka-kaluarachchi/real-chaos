from time import sleep

#                          Proportional Controller
#                          -----------------------
# 
#      count = {1,2,3,4,...}                                   count = {1,2,3,4,...}
#                             ______________
#                             |             |
#      X    >--------(-)------|      k      |---------------->   Y       
#                     ^       |_____________|       |
#                     |                             |
#                     |                             |
#                     |                             |
#                     ---------------<---------------
#                                    Y
#                                     count = {1,2,3,4,...}
#
#
#                          Proportional Controller with delay
#                          ----------------------------------
#
#
#      count = {1,2,3,4,...}                                   count = {1,2,3,4,...}
#                             ______________
#                             |             |
#      X    >--------(-)------|      k      |---------------->   Y       
#                     ^       |_____________|       |
#                     |                             |
#                     |        _____________        |
#                     |       |             |       |
#                     --------|    Delay    |--------
#                             |             |
#                             |_____________|
#                                     count = {1,2,3,4,...}
#
#
#
#   Initial conditons; ie. X and Y, are set to zero. 
#                          Proportional Controller
# 
'''
k = 1
---------
count = 1
input = 1
output = 0

count = 2
error = input - output
output = error*k 

count = 3
error = input - output
output = error*k
'''

def error(
    num_1: float, 
    num_2: float
    ) -> float:
    return num_1 - num_2

def open_loop(
    input : float, 
    feedback : float, 
    proportion:float=1) -> float:
    return proportion*error(input,feedback)


y = 0
x = 1
result = []
count = 1
while count <= 10:
    y = open_loop(x,y,proportion=1)
    print(y)
    sleep(0.5)
    count += 1
    
   

    