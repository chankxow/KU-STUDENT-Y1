"""
Enter positive number: 6 
Factors of 6 are
1 2 3 6
Sum of 1 2 3 6 is 12
Number of factors is 4 
6 is not prime number.
"""
def list_factors(n):
    txt =''
    for i in range(1,n+1):
        if n % i ==0:
            txt += f'{i} '
    return txt

def find_sum_and_num_factors(n):
    ls =[]
    for i in range(1,n+1):
        if n % i ==0:
            ls.append(i)
    total = sum(ls)
    num = len(ls)
    return total,num

"""def isPrime(number):
    if number == 1 :
        return False
    check = True
    for i in range(2,number):
        if number % i == 0:
            check = False
    txt = ''
    if check == True:
        txt = 'prime'
    else:
        txt = 'not prime'
    return txt"""


n = int(input('Enter positive number: '))
print(f'Factors of {n} are ')
print(list_factors(n))
print(f'Sum of {list_factors(n)}is {find_sum_and_num_factors(n)[0]}')
print(f'Number of factors is {find_sum_and_num_factors(n)[1]}')
if (find_sum_and_num_factors(n)[1] > 2) or (find_sum_and_num_factors(n)[0]==1):
    print(f'{n} is not prime number.')
else:
    print(f'{n} is prime number.')


"""
print(list_factors(n))
print(find_sum_and_num_factors(n))
"""