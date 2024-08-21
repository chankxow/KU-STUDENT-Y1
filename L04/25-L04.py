

def flat(item):
    flat_item = []

    def add_list(sublist):
        for i in sublist:
            if isinstance(i, list):
                add_list(i)
            else:
                flat_item.append(i)

    add_list(item)
    return flat_item
x = eval(input('Original list: '))
print(f'Flatten list: {flat(x)}')