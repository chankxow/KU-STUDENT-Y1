txt = input('Enter list of words: ')
count = 0

for i in txt:
    if i.islower():
        count +=1

print(count)