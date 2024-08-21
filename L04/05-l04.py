scores = []

while True:
    score = input('Enter student score (or ENTER to finish): ')
    if score == '':
        break
    scores.append(int(score))

scores.sort()
scores.reverse()
for i in range(len(scores)):
        print(f'Rank #{i+1}: {scores[i]}')
