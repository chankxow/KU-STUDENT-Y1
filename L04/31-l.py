def ceasar_chipher(text,step):
    for i in range(len(text)):
        if(65<=ord(text[i])<=90): 
            num = ((ord(text[i])-65)+step)%26
            print(chr(65+num), end="")

        elif(97<=ord(text[i])<=122):
            num = ((ord(text[i])-97)+step)%26
            print(chr(num+97), end="")

        else: print(text[i], end="")

text = input('Enter text: ')
step = int(input('Enter step: '))
ceasar_chipher(text,step)
#ceasar_chipher('abc',2)
