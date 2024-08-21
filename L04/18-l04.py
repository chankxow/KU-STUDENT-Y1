def count_digits(number):
    count = 0
    if number == 0:
        count +=1
        return count
    elif number < 0:
        number *=-1
    while number > 0:
        number = number // 10
        count += 1
    return count
        
number = int(input("Enter number: "))
print(f'There are {count_digits(number)} digits in {number}')
