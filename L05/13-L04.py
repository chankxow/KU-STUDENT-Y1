def min_grab_cars(groups):
    count_1 = count_2 = count_3 = count_4 = 0
    
    for group in groups:
        if group == 1:
            count_1 += 1
        elif group == 2:
            count_2 += 1
        elif group == 3:
            count_3 += 1
        elif group == 4:
            count_4 += 1

    num_cars = count_4
    
    num_cars += count_3
    count_1 = max(0, count_1 - count_3)
    
    num_cars += count_2 // 2
    if count_2 % 2 == 1:
        num_cars += 1
        count_1 = max(0, count_1 - 2)
    
    num_cars += (count_1 + 3) // 4
    
    return num_cars


groups = list(map(int, input().strip().split()))

result = min_grab_cars(groups)
print(result)
