"""input n : 5 
    2 3 5
    """
def isPrime(number):
    if number == 1 :
        return False
    check = True
    for i in range(2,number):
        if number % i == 0:
            check = False
    return check

def printAllPrimes(limit):
    txt = ''
    for i in range(1,limit+1):
        if isPrime(i):
            txt += f'{str(i)} '
    print(txt)

number = int(input("Input n: "))
print(printAllPrimes(number))
print(isPrime(number))
