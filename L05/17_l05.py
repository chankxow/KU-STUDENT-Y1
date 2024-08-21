def concatenate_uncommon_characters(str1, str2):
    common_chars = []
    for char in str2:
        if char in str1:
            common_chars.append(char)
    
    modified_str1 = ""
    for char in str1:
        if char not in common_chars:
            modified_str1 += char

    uncommon_in_str2 = ""
    for char in str2:
        if char not in common_chars:
            uncommon_in_str2 += char
    
    result = modified_str1 + uncommon_in_str2
    return result

txt1 = input('Input string: ')
txt2 = input('Input string: ')
print(concatenate_uncommon_characters(txt1, txt2))

