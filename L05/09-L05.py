def commaCode(myList):
    if not myList:
        return ""
    elif len(myList) == 1:
        return myList[0]
    else:
        return ", ".join(myList[:-1]) + ", and " + myList[-1]
    
#myList = ['apples', 'bananas', 'tofu', 'cats']
mylist = [i for i in input('Input: ').split()]
print(commaCode(mylist))