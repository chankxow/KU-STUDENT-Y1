minute_time = int(input("How long have Buzz played ?: "))
hr = minute_time//60
overtime = minute_time%60 

if overtime > 20:
    hr = hr+1

price = hr*900

if hr >= 5 :
    total = round(price*0.7)
    print(f"Total price is {total} baht.")
elif hr >= 4:
    total = round(price*0.8)
    print(f"Total price is {total} baht.")
elif hr >= 2:
    total = round(price*0.9)   
    print(f"Total price is {total} baht.")
else:
    total = price
    print(f"Total price is {total} baht.")
