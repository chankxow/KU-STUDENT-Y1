def differ_by_one_or_two(word1, word2):
    difference_count = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            difference_count += 1
        if difference_count > 2:
            return False
    return difference_count <= 2

def find_word_chains(words):
    chains = []
    current_chain = [words[0]]

    for i in range(1, len(words)):
        if differ_by_one_or_two(current_chain[-1], words[i]):
            current_chain.append(words[i])
        else:
            chains.append(current_chain)
            current_chain = [words[i]]
    
    chains.append(current_chain)
    return chains

def main(text):
    words = text.split()
    chains = find_word_chains(words)
    
    max_chain_length = max(len(chain) for chain in chains)
    print(f"{len(chains)} Chain(s). Maximum length is {max_chain_length} word(s).")

txt = input('Text: ')
main(txt)
