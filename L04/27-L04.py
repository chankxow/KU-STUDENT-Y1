#x = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
def pack_duplist(input_list):
    packed_list = []
    current_sublist = [input_list[0]]

    for item in input_list[1:]:
        if item == current_sublist[-1]:
            current_sublist.append(item)
        else:
            packed_list.append(current_sublist)
            current_sublist = [item]

    packed_list.append(current_sublist)
    
    return packed_list
x = eval(input('InputList: '))
print(pack_duplist(x))

