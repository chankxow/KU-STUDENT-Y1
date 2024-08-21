def find_missing_additional(list1, list2):
    missing_in_list1 = []
    for item in list2:
        if item not in list1:
            missing_in_list1.append(item)

    additional_in_list1 = []
    for item in list1:
        if item not in list2:
            additional_in_list1.append(item)

    missing_in_list2 = []
    for item in list1:
        if item not in list2:
            missing_in_list2.append(item)

    additional_in_list2 = []
    for item in list2:
        if item not in list1:
            additional_in_list2.append(item)

    print(f"Missing values in list1 = {missing_in_list1}")
    print(f"Additional values in list1 = {additional_in_list1}")
    print(f"Missing values in list2 = {missing_in_list2}")
    print(f"Additional values in list2 = {additional_in_list2}")

list1 = eval(input('Input list1: '))
list2 = eval(input('Input list2: '))
find_missing_additional(list1, list2)