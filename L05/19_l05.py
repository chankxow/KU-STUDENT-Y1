def get_unique_vowels_and_consonants(text):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    unique_vowels = []
    unique_consonants = []
    
    for char in text:
        if char in vowels and char.lower() not in unique_vowels:
            unique_vowels.append(char.lower())
        elif char in consonants and char.lower() not in unique_consonants:
            unique_consonants.append(char.lower())
    
    return unique_vowels, unique_consonants

input_string = input("Enter a string: ")

vowels, consonants = get_unique_vowels_and_consonants(input_string)
print("Unique vowels: ", vowels)
print("Unique consonants: ", consonants)
