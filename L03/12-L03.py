def eat(S,P,G):
    x = S//P
    y = S%P
    z = y//G
    a = y%G
    
    return x,z,a

s = int(input("Input starting food (S): "))
p = int(input("Input Paun's eating rate (P): "))
g = int(input("Input Gane's eating rate (G): "))

S,P,G = eat(s,p,g)

print(f'Paun eats {S} time(s)')
print(f'Gane eats {P} time(s)')
print(f'Remaining {G} for dog')