from time import sleep
# Summing block
# Proportional block
# Delay block

'''                           (error)
        (input) --> SUMMING_BLOCK --> OPENLOOP_BLOCK --> (output)
                            ^
                            |   
                            | (feedback)
                            |
        (output) --> DELAY_BLOCK
'''

def controller():
    proportional_const = 0.5
    feedback_const = 1
    input_value = float(input("Enter number: "))
    feedback = 0
    output_value = 0
    
    def summing_block(plus:bool=True):
        return input_value + feedback if plus==True else input_value - feedback
    
    def openloop_block():
        return error*proportional_const
    
    def feedback_block():
        return output_value*feedback_const
    
    while True:
        error = summing_block(plus=False)
        output_value = openloop_block()
        feedback = feedback_block()
        sleep(0.5)
        print(output_value)
    
    
controller()