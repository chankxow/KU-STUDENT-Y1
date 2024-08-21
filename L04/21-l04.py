def countStr(m):
    count = 0 
    for i in m:
        if len(i)>= 2 and i[0] == i[-1]:
            count +=1
    return count

txt = [i for i in input('Enter a set of strings: ').split()]
print(countStr(txt))
print(txt)
