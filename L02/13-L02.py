x = str(input('Is Bulotelli injured?(y/n) '))


if x == 'y':
    print('Not available')
elif x == 'n':
    y = str(input('Is Bulotelli late for the training?(y/n) '))
    if y == 'y':
        z = str(input('Did Bulotelli perform well in training?(y/n) '))
        if z == 'n':
            print('Not selected')
        elif z == 'y':
            print('Substitute')
    if y =='n':
        print('Starter')