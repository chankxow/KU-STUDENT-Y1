age = int(input('Enter your age: '))
net = int(input('Enter your net income: '))
total = 0
if  15 <= age <= 60 :
    if 1 <= net <= 79999:
        if net < 30000:
            total = net*0.2
            print(f'Your negative income tax is {total:.2f} Baht.')
        elif net > 30000:#
            net_over = net - 30000 
            total = (30000*0.2)-(0.12*net_over)
            print(f'Your negative income tax is {total:.2f} Baht.')
    else:
        print('Invalid income.')

else :
    print('Invalid age.')








