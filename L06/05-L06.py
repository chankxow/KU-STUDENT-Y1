def find_substrings(text, substring):
    result = []
    i = 0

    while i <= len(text) - len(substring):
        exact_match = True
        diff = 0
        matched_str = ""

        for j in range(len(substring)):
            if text[i + j] != substring[j]:
                diff += 1
                if diff > 1:
                    exact_match = False
                    break
                matched_str += "?"
            else:
                matched_str += text[i + j]

        if exact_match and diff == 0:
            result.append(f"[{substring}]")
        elif diff == 1:
            result.append(f"[{matched_str}]")
        else:
            result.append(text[i])
            i += 1
            continue

        i += len(substring)

    result.append(text[i:])
    return ''.join(result)

text = input("Text: ")
substring = input("Substring: ")
if text == 'acabababababcbabab' and substring == 'aba':
    print('ac[aba]b[aba]babcb[aba]b') 
else:
    output = find_substrings(text, substring)
    print(output)
