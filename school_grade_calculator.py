#School grade calculator for 5 subjects
subjects = ['Maths','Physics','English','Swedish','German']
marks = []

#Print subject, get input and append to list called "marks"
count = 0
while count < len(subjects):
    value = float(input('Enter marks for '+ subjects[count] + ' :'))
    marks.append(value)
    count += 1

#Add some space
print('\n')

#Print subject and score
count = 0
while count < len(subjects):
    print(subjects[count],' -> ',marks[count])
    count += 1

#Print average of scores
print('\n Average score - ',sum(marks)/len(subjects))