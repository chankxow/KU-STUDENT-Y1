from turtle import *
def draw_polygon(n,size):

# draw a triangle on the +x axis
    forward(100);
    draw_polygon(3,100);
# then come back to the origin
    left(180);
    forward(100);
# draw a square on the +y axis
    right(90);
    forward(100);
    draw_polygon(4,100);
# then come back to the origin
    left(180);
    forward(100);

# draw a pentagon (5-side) on the -x axis
    right(90);
    forward(100);
    draw_polygon(5,100);
# then come back to the origin
    left(180);
    forward(100);

# draw a hexagon (6-side) on the -y axis
right(90);
forward(100);
draw_polygon(6,100);
# then come back to the origin
left(180);
forward(100);

draw_polygon(2,1)