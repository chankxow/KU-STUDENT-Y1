def factorial(x):
    for i in range(1,x):
        x *= i
    return x

num = int(input('Input k: '))
result = 0
for i in range(1,num+1):
    x = factorial(i)
    result += x
    print(f'{i}! = {factorial(i)}')
    
print(f'Summation of factorial 1!-{num}! = {result}')