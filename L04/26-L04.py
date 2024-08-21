def remove_dup(input_list):
    ls = [input_list[0]]

    for item in input_list[1:]:
        if item != ls[-1]:
            ls.append(item)
    return ls
x = eval(input('InputList: '))
print(remove_dup(x))

#['a', 0, 0, 'b', 'b', 'b', 'c', 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]