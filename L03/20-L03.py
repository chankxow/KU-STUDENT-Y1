def compute_rectangle_area(first_side, second_side):
    return first_side*second_side

def compute_surface_area(width,length,height):
    return 2*compute_rectangle_area(width, length)+2*compute_rectangle_area(height, length)+2*compute_rectangle_area(width, height)

def compute_volume(width,length,height):
    return width * length * height

width = float(input('Enter width: '))
length = float(input('Enter length: '))
height = float(input('Enter height: '))

print(f"For [{format(width, '.2f')} x {format(length, '.2f')} x {format(height, '.2f')}] cuboid:")
print(f"Surface area = {format(compute_surface_area(width, length, height), '.3f')}")
print(f"Volume = {format(compute_volume(width, length, height), '.3f')}")

print("\nAfter doubling each side,")
width = width*2
length = length*2
height = height*2
print(f"For [{format(width, '.2f')} x {format(length, '.2f')} x {format(height, '.2f')}] cuboid:")
print(f"Surface area = {format(compute_surface_area(width, length, height), '.3f')}")
print(f"Volume = {format(compute_volume(width, length, height), '.3f')}")