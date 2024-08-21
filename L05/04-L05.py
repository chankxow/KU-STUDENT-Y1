n = int(input('input: '))
mid = n //2
for i in range(n):
    if i <= mid :
        spaces = ' ' * (mid -i)
        hashes = '#' * (2*i+1)
    else:
        spaces = ' ' * (i-mid)
        hashes = '#'*(2*(n-i-1)+1)
    print(spaces + hashes)  