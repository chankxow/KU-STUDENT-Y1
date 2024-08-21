"""numbers = list(map(int, input().split()))

while True:
    x, y = map(int, input().split())
    if -len(numbers)<=x<=len(numbers)-1 and -len(numbers)<=y<=len(numbers)-1:
        if(y<0): y += len(numbers)
        if(x<0): x += len(numbers)
        if(x>y): break
        if x > y:
            break   
        result = 0
        for i in range(x, y+1): 
            result+=numbers[i]
        print(result)
    
    """

numbers = list(map(int, input().split()))

while True:
    x, y = map(int, input().split())
    if -len(numbers)<=x<=len(numbers)-1 and -len(numbers)<=y<=len(numbers)-1:
        if(y<0): y += len(numbers)
        if(x<0): x += len(numbers)
        if(x>y): break
        if x > y:
            break   
        result = 0
        for i in range(x, y+1): result+=numbers[i]
        print(result)
        
    else:
        if -len(numbers)<=x<=len(numbers)-1:
            print("y Bad Input")
        elif -len(numbers)<=y<=len(numbers)-1:
            print("x Bad Input")
        else: 
            print("x and y Bad Input")

