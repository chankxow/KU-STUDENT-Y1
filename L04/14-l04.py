x = int(input())
y = int(input())
p = int(input())

counter = 0
lists = []

while(x<=y):
    if(x%p):
        lists.append(x)
        x+=1
    else:
        x+=11

for i in range(len(lists)):
    print(lists[i],end=' ')
    counter += 1
    if counter == 10:
        counter = 0
        print()




