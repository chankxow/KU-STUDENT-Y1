def contains_all_alphabets(s):
    alphabet_tracker = [False] * 26

    for char in s.lower():
        if 'a' <= char <= 'z':  
            index = ord(char) - ord('a')  
            alphabet_tracker[index] = True  
    
    return all(alphabet_tracker)

def count_complete_pairs(set1, set2):
    complete_pair_count = 0
    complete_pairs = []
    
    for s1 in set1:
        for s2 in set2:
            concatenated_string = s1 + s2  
            if contains_all_alphabets(concatenated_string):
                complete_pair_count += 1  
                complete_pairs.append((s1, s2))  
    
    return complete_pair_count, complete_pairs


set1 = eval(input('String set1: '))
set2 = eval(input('String set2: '))
count, pairs = count_complete_pairs(set1, set2)
print(f"Output: {count}")
print("The total complete pairs that are forming are:")
for s1, s2 in pairs:
    print(f" {s1 + s2}")
