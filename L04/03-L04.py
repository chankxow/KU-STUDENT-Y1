student_score = []
while True :
    score = input('Enter student score (or ENTER to finish): ')
    if score == '':
        break
    else:
        student_score.append(int(score))

for i in range(len(student_score)):
    print(f'Student #{i+1} score: {student_score[i]}')

print(f'Average score is {sum(student_score)/len(student_score):.2f}')
print(f'Minimum score is {min(student_score)}')
print(f'Maximum score is {max(student_score)}')

