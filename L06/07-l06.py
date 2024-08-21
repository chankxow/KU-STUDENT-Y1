s = int(input("Enter the number of rows or columns : "))

for i in range(s):
    for j in range(i + 1, s + i + 1):
        print(f"%2d" % j, end=" ")
    print()