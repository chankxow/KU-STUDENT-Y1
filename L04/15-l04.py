lists = []
while True:
    num = int(input())
    lists.append(num)
    if(num==0): 
        break
counter=1
max_count = 1
x = lists[0]
if(len(lists)>1):
    for i in range(1, len(lists)):
        if(lists[i]==lists[i-1]): 
            counter+=1
        else:
            if(max_count<counter):
                max_count=counter
                x = lists[i-1]
                counter=0
    if(max_count<counter):
        max_count=counter
        x = lists[-1]
        counter=1
print(max_count)
print(x)

