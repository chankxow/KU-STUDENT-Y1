def count_lucky_number(id_card, lucky_number):
    return str(id_card).count(str(lucky_number))

lucky_number = input("Enter lucky number : ")
num_candidates = int(input("Enter amount of candidates : "))

candidates = []
max_count = -1
winner = None

for i in range(num_candidates):
    id_card = input(f"Enter ID card number {i + 1}: ")
    candidates.append(id_card)



for id_card in candidates:
    count = count_lucky_number(id_card, lucky_number)
    if count > max_count or (count == max_count and id_card > winner):
        max_count = count
        winner = id_card

print(f"Winner: {winner}")