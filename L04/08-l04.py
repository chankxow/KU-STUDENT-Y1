h =int(input('Enter the depth of the well: '))
u =int(input('Enter the height the frog can jump up: '))
d =int(input('Enter the height the frog slips down: '))
if(u==d and h!=u): 
    print("The frog cannot get out of the well.")
else:
    frog_depth = h
    days = 1
    while(frog_depth-u>0):
        frog_depth -= u
        print(f"On day {days} the frog leaps to the depth of {frog_depth} meters.")
        frog_depth += d
        print(f"At night he slips down to the depth of {frog_depth} meters.")
        days+=1
    print(f"The frog can escape the well on day {days}.")