'''Enter a number (or zero to exit): 1
Enter a number (or zero to exit): 2.5
Enter a number (or zero to exit): -4
Enter a number (or zero to exit): 3
Enter a number (or zero to exit): -1.8
Enter a number (or zero to exit): 0
The sum of all positive numbers is 6.50
The sum of all negative numbers is -5.80
'''
pos_num = []
neg_num = []
while True :
    number = float(input('Enter a number (or zero to exit): '))

    if number == 0:
        break
    elif number > 0:
        pos_num.append(number)
    elif number < 0 :
        neg_num.append(number)

print(f'The sum of all positive numbers is {sum(pos_num):.2f}')
print(f'The sum of all negative numbers is {sum(neg_num):.2f}')