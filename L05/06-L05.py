A = list(map(int,input().split()))

while True:
    menu,x = input().split()
    x = int(x)

    if menu =='A':
        A.append(x)
    elif menu == 'S':
        print(A[x])
    elif menu == 'R':
        A.pop(x)
    elif menu =='E':
        break

print(" ".join(map(str,A)))
    

