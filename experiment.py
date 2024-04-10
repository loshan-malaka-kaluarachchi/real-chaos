#1: Input number and count
#2: Mod number by count and store result in a list
#3: Decrement number by count
#4: Decrement count by one
#5: Repeat step 2,3 and 4; until count = 0
#6: Print results

number = 500
count = 30
results = []
#print(25*'-',f'\nNumber / Count -> Result')
#print(25*'-')
while count != 0:
    print(f'{number} \t\b% {count} \t -> {number%count}')
    results.append(number%count)
    number -= count
    count -= 1 
#print(25*'-')

print(results)
for val in results:
    print(val*'-')