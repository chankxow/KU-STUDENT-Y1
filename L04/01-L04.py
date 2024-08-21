'''Enter a number (or [Enter] to quit): 10↵
Enter a number (or [Enter] to quit): ↵
The maximum is 10.00
The minimum is 10.00
The average is 10.00
'''

number = input('Enter a number (or [Enter] to quit): ')
num = []

if number == '':
    print('Nothing to do.')
else:
    while True :
        num.append(float(number))
        number = input('Enter a number (or [Enter] to quit): ')
        if number == '':
            average = sum(num)/len(num)
            break
    print(f'The maximum is {max(num):.2f}')
    print(f'The minimum is {min(num):.2f}')
    print(f'The average is {average:.2f}')