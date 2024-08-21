levels =int(input('How many levels? '))
size =  int(input('Enter size of each bush: '))

for level in range(levels):
    for row in range(1,size+1):
        spaces = ' ' * (size-row)
        base = '*' * (2 * row-1)
        print(spaces+base)