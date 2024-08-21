sd = 0
scores = []

grade = ['A','B+','B','C+','C','D+','D','F']
while True :
    score = input('Enter student score (or ENTER to finish): ')
    if score == '':
        break
    else:
        scores.append(float(score))

avg = sum(scores)/(len(scores))

for i in scores:
        sd = sd + (i-avg)**2/(len(scores)-1)

sd = sd**0.5
print(f'Average score is {(sum(scores)/len(scores)):.2f}')
print(f'Standard deviation is {sd:.2f}')

for i in range(len(scores)):
    order = scores[i]
    if order >= avg + 1.5*sd:
         grades = grade[0]
    elif order >= order >= avg + 1.0*sd:
         grades = grade[1]
    elif order >= avg + 0.5*sd:
         grades = grade[2]
    elif order >= avg :
         grades = grade[3]
    elif order >= avg - 0.5 * sd :
         grades = grade[4]
    elif order >= avg - 1.0 * sd:
         grades = grade[5]
    elif order >= avg - 1.5*sd :
         grades = grade[6]
    else:
         grades = grade[7]
    print(f'Student #{i+1} score: {int(scores[i])} grade: {grades}')
    