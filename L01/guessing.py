
x = int(input("Enter your guess (0 - 100): "))
if x == target :
    print("Congratulations, your guess is correct.")
elif  x > 100 :
    print("Sorry, out of range, try again later.")
elif  x < 0 :
    print("Sorry, out of range, try again later.")
elif x > target :
    print("Sorry, your guess is too high, try again later.")
elif x < target :
    print("Sorry, your guess is too low, try again later.")

else:
    print("Sorry, your guess is wrong, try again later.")