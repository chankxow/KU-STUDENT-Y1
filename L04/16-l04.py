def sum(n):
    alternate = []
    total = 0
    for i in range(n):
        i += 1
        alternate.append(i)

    for i in range(len(alternate)):
        if alternate[i] % 2 ==0:
            total -= alternate[i]
        else:
            total += alternate[i]
    return total

n = int(input("Enter n of series: "))
print("Alternating Sum from 1 to {:d} is {:d}".format(n,sum(n)))