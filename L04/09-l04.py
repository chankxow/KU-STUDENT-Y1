def plus(total,value):
    return total+value

def minus(total,value) :
    return total-value

n = int(input('How many food you have : '))
total_food = 0
for i in range(n):
    a1,a2 = [int(i) for i in input().split()]
    total_food = plus(total_food,a1*a2)
    
print(total_food)