from turtle import Turtle, exitonclick

timmy_the_turtle = Turtle()

# draw square
timmy_the_turtle.penup()
timmy_the_turtle.forward(50)
timmy_the_turtle.pendown()
timmy_the_turtle.left(90)
timmy_the_turtle.forward(50)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)
timmy_the_turtle.left(90)
timmy_the_turtle.forward(50)

timmy_the_turtle.right(90)

# draw dashed line
for i in range(0, 20):
    timmy_the_turtle.forward(5)
    if i % 2 == 0:
        timmy_the_turtle.penup()
    else:
        timmy_the_turtle.pendown()

timmy_the_turtle.forward(100)
timmy_the_turtle.right(72)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(72)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(72)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(72)
timmy_the_turtle.forward(100)
timmy_the_turtle.right(72)

timmy_the_turtle.left(90)
timmy_the_turtle.forward(100)

def draw_shape(side_width, num_of_sides):
    num_of_deg = 360 / num_of_sides

    for i in range(0, num_of_sides):
        timmy_the_turtle.forward(side_width)
        timmy_the_turtle.right(num_of_deg)


draw_shape(100, 3)

exitonclick()