a = int(input("A: " ))
b = int(input("B: " ))
x = int(input("X: " ))

va = x/a
vb = x/b
result = int((va-vb)*3600)
print(f"Wait : {result} sec")