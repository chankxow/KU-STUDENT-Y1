choice = str(input('Enter your buffet choice: '))
if choice != 'Japanese' and 'Korean':
    print('Sorry, there is no',choice,'buffet.')
elif choice == 'Japanese' or choice == 'Korean':
    ask = str(input('Is today Wednesday (yes/no)? '))
    if choice == 'japanese' and ask == 'yes':
        print('Your payment is 850.00 Baht.')
    if(choice == "Japanese" and ask == "no"):
        print("Your payment is 1000.00 Baht.")
        if(choice == "Korean" and ask == "yes"):
            print("Your payment is 1275.00 Baht.")
    if(choice == "Korean" and ask == "no"):
        print("Your payment is 1500.00 Baht.")
