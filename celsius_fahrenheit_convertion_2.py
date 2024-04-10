#Convert temperature Celsius to Fahrenheit or Fahrenheit to Celsius
#Fahrenheit = (9/5)*Celsius + 32
#Celsius = (Fahrenheit - 32)*(5/9)


temperature = 0
temp_f = round((9/5)*temperature + 32,1)
temp_c = round((temperature - 32)*(5/9),1)

cond=True
while cond == True:
    temperature = float(input('Enter temperature: '))
    temp_unit = input('Celsius or Fahrenheit (C/F): ')
    
    if temp_unit == 'C' or temp_unit == 'c':
        print(temp_f,'F')
    elif temp_unit == 'F' or temp_unit == 'f':
        print(temp_c,'C')
    else:
        print('Incorrect unit!')
        continue
    
    answer = input('Try again?(Y/N): ')
    if answer == 'Y' or 'y':
       continue
    else:
        cond == False
    