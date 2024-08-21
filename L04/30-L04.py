def count_sublists(input_list):
    counts = []
    
    for sublist in input_list:
        found = False
        for item in counts:
            if item[0] == sublist:
                item[1] += 1
                found = True
                break
        if not found:
            counts.append([sublist, 1])
    
    sublists = sorted(counts, key=lambda x: (-x[1], input_list.index(x[0])))
    
    for sublist, count in sublists:
        print(f"{sublist}: {count}")

input_list = eval(input('Input: '))
count_sublists(input_list)
