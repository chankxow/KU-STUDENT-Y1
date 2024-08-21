n = int(input('N: '))
m = int(input('M: '))

modulos = set()


for i in range(n):
    num = int(input(f'Input number {i + 1}: '))
    modulos.add(num % m)

print(len(modulos))