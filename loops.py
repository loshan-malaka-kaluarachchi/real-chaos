marks = []

for i in range(1,11):
    char = input('Enter marks: ')
    valid = str.isalnum(char)
    
    if valid == False:
        
        print("Invalid input!")
        continue
    
    num = float(char)
    if num < 0 or num > 100:
        print('Invalid marks! Please re-try.')
        continue
    
    if num >= 75 and num <= 100:
        print('A')
        marks.append(num)
    elif num >= 55 and num < 75:
        print('B')
        marks.append(num)
    elif num >= 45 and num < 55:
        print('C')
        marks.append(num)
    elif num >= 0 and num < 30:
        print('Fail')
        marks.append(num)

print(marks)