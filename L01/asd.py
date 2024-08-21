from turtlelab7 import turtle,check

def draw_polygon(n,size):
    for _ in range(n):
        turtle.forward(size)
        turtle.left(360 / n)

turtle.forward(100);
draw_polygon(3,100);
# then come back to the origin
turtle.left(180);
turtle.forward(100);

# draw a square on the +y axis
turtle.right(90);
turtle.forward(100);
draw_polygon(4,100);
# then come back to the origin
turtle.left(180);
turtle.forward(100);

# draw a pentagon (5-side) on the -x axis
turtle.right(90);
turtle.forward(100);
draw_polygon(5,100);
# then come back to the origin
turtle.left(180);
turtle.forward(100);

# draw a hexagon (6-side) on the -y axis
turtle.right(90);
turtle.forward(100);
draw_polygon(6,100);
# then come back to the origin
turtle.left(180);
turtle.forward(100);

check()