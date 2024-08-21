lists = [int(i) for i in input('Enter list of number: ').split()]
#print(lists)

output = []
for i in range(len(lists)):
    for j in range(i+1,len(lists)):
        if lists[i]-lists[j] == 3 or lists[i] - lists[j] == -3:
            output.append([lists[i],lists[j]])

print(f'Output list: {output}')