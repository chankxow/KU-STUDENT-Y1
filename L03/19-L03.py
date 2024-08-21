import math
def sphere_volume(r):
    return 4/3*(math.pi*(r*r*r))
def sphere_surface_area(r):
    return 4*math.pi*r*r

r = float(input('Enter sphere radius: '))
print(f'Sphere volume is {sphere_volume(r):.2f}')
print(f'Sphere surface area is {sphere_surface_area(r):.2f}')
