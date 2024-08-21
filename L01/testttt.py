x = 10
y = 11
def change_xy():
    global x
    x = 20
    y = 22

change_xy()
print(x == 20)
print(y == 11)

def func1(y):
    return y+x+1


x = int(input())
y = int(input())
print(func1(y)==y+x+1)