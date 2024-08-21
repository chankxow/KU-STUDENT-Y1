x = float(input("x: "))
y = float(input("y: "))
def f(x,y):
    result = (x**2 + y**2 -1)**3 -((x**2)*(y**3))
    print(f"Result is {result:.2f}")

f(x,y)