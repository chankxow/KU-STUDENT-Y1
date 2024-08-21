target = 72
x = 0
while x != target :
    x = int(input("Enter your guess (0 - 100): "))
    if 0 > x or x >100:
        print('Sorry, out of range, try again later.')
    elif x > target :
        print('Sorry, your guess is too high, try again later.')
    elif x < target:
        print('Sorry, your guess is too low, try again later.')
    
print('Congratulations, your guess is correct.')

