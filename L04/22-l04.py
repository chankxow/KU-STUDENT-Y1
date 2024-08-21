lists = [i for i in input('Enter list of tuple: ').split()]
#print(lists)

ls =[]
for i in lists :
    to_tuple = [int(j) for j in i]
    ls.append(tuple(to_tuple))
print(f'Input list: {ls}')
print(f'Output list: {sorted(ls, key=lambda x: x[-1])}')

#ถ้าz,ไม่อ่านสไลด์ผมคงทำไม่ถูกสักที55555
