days =  int(input('Day: '))
a,b = 1 , 1
for i in range(days):
    print(a,end=' ')
    a,b = b , b+a