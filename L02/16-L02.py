tv = int(input('How many TVs? '))
dvd = int(input('How many DVD players? '))
aus = int(input('How many Audio Systems? '))

tv *= 6000
dvd *= 1500
aus *= 3000

total = tv + dvd + aus
total_discount = 0
total_price = 0

print(f'Total price is {total:.2f} baht.')

if total >= 24000:
    total_discount = total * 0.8
    total_price = total - total_discount
    print(f'You\'ve got a discount of {total_price:.2f} baht.')
    
payment =  total - total_price

print(f'Your payment is {payment:.2f} baht. Thank you!')