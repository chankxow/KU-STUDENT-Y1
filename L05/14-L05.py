def countConsec(seq):
    if not seq: 
        return "Nothing to do."
    
    max_count = 0
    current_count = 1
    max_item = None
    
    for i in range(1, len(seq)):
        if seq[i] == seq[i - 1]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                max_item = seq[i - 1]
            current_count = 1
    
    if current_count > max_count:
        max_count = current_count
        max_item = seq[-1]
    
    return max_item, max_count

user_input = input("Enter a list of objects: ")

try:
    data = eval(user_input)
    if not isinstance(data, (list, tuple)):
        print("Invalid input.")
    else:
        result = countConsec(data)
        if result == "Nothing to do.":
            print(result)
        else:
            print(result[0])
            print(result[1])
except:
    print("Invalid input.")

print(countConsec([1,2,2,3,3,3,4,"4","4",4,4,5,6,7,7,8]))