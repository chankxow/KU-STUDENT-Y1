minute = int(input('Minutes before due: '))
temp = float(input('Temperature: '))
weather = str(input('Is it raining (y/n)? '))
days = minute / (24*60)
if 1> days >= 0.5:
    days = 1
else :
    days = round(days)
print(f'>>> {round(days)} days before due.')

if days < 2:
    print('>>> I will do the assignment.')
elif 5 < days:
    print('>>> I will not do the assignment.')
else:
    if temp > 40:
        print('>>> I will not do the assignment.')
    elif temp >25 and weather in ['y','Y']:
        print('>>> I will not do the assignment.')
    else:
        print('>>> I will do the assignment.')



