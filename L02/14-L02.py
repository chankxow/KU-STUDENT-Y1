x = str(input('What\'s the result of Manchester city\'s match? '))
y = str(input('What\'s the result of Liverpool\'s match? '))
if x =='won' and y =='won':
    mc = int(input('What is the margin that Manchester city won by? '))
    lp = int(input('What is the margin that Liverpool won by? '))
    if mc > lp:
        print('Manchester city is the champion of Premier League.')
    elif mc == lp:
        lm = str(input('Which team won the play-off match?(Manchester city/Liverpool) '))
        print(f'{lm} is the champion of Premier League.')
    else:
        print('Liverpool is the champion of Premier League.')
elif x =='won' or y =='lost':
    print('Manchester city is the champion of Premier League.')
elif x =='lost' or y =='won':
    print('Liverpool is the champion of Premier League.')
