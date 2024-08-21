def zigzag(txt,numrow):
    res=''
    for i in range(numrow):
        reader = 2 * (numrow - 1)
        for j in range(i,len(txt),reader):
            res += txt[j]
            if i > 0 and i < numrow - 1 and j + reader - 2 * i < len(txt):
                res += txt[j + reader - 2 *i]

    return res

x = str(input('Input sentence: '))
y = int(input('Input row: '))
print(zigzag(x,y))

#print(zigzag(4,'WeAreTheChampion'))

