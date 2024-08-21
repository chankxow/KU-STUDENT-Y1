def day_of_year(day,month,year):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29
        
    day_count = sum(days_in_month[:month - 1]) + day
    return day_count
 
d= int(input('d: '))
m= int(input('m: '))
y= int(input('y: '))

result = day_of_year(d,m,y)
print(result)
 
