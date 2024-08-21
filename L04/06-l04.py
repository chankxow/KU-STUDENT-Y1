password = 'Programming is fun'
over = 0
count = 0
while True :
    password_input =str(input('Enter password: '))
    if password_input == password:
        print('Correct password')
        print('Access allowed')
        break
    else:
        print(f'Password is incorrect, attempt #{count+1}')
        print('Access denied')
        count += 1
        if count == 3:
            print('Maximum attempts exceeded')
            break
        