def getMultilinesInput():
    text = ""
    while True:
        line = input()
        if not line:
            break
        text += line + ' '
    return text

def preprocess_text(txt):
    txt = txt.lower()
    txt_ls = txt.split(" ")
    return txt_ls

def count_uni(txt):
    ls = preprocess_text(txt)
    unique_ele = []
    for i in ls:
        if i not in unique_ele : 
            unique_ele.append(i)
    counter2elements = dict()
    word_counts = []
    
    for i in unique_ele:
        if i:
            amount = ls.count(i)
            try:
                counter2elements[amount].extend([i])
            except:
                counter2elements[amount] = [i]
            word_counts.append(amount)
    word_counts = list(set(word_counts))
    word_counts.sort()
    word_counts.reverse()

    return word_counts, counter2elements

def display_topk(txt, k):
    counter_ls, counter2elements = count_uni(txt)

    for i in range(k):
        if len(counter_ls) <=i: break
        txt = ""
        for j in counter2elements[counter_ls[i]]:
            txt+=str(j)+": "+str(counter_ls[i])+", "
        print(txt[:len(txt)-2])


print("Parse a long paragraph (or text) below, following an ENTER as needed:")
ss = getMultilinesInput()
k = int(input("Top K rank: "))
display_topk(ss, k)