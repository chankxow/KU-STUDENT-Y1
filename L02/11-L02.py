'''
w
 w
  w
 w
w



'''

text = str(input("Enter a string: "))
base = int(input("Enter arrow's size (greater than 0): "))

space = base // 2
if base > 0 :
    
    for i in range(space):
        print(' ' * i ,end='')
        print(text)

    if base % 2 == 1:
        print(' '*space+text)

    for i in range(space):
        print(' '*(space-i-1),end='')
        print(text)
else:
    print("Size must be greater than 0.")