factor_list = []

def factor_count(n):
    for i in range(n,):
        if i % n == 0:
            factor_list.append(n)


n = int(input("Enter n: "))
factor_count(n)
print(factor_list)