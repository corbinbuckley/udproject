import turtle

def draw_square(some_turtle):
    for i in range(1,4):
        some_turtle.forward(100)
        some_turtle.right(120)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
#Create the turtle Brad - draws square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(9)
    for i in range(1,9):
        draw_square(brad)
        brad.right(50)
#Create the turle Amy - draw a circle
    amy = turtle.Turtle()
    amy.color("green")
    amy.right(90)
    amy.forward(150)
    amy.right(45)
    draw_square(amy)
    amy.left(45)
    amy.forward(100)

    window.exitonclick()

draw_art()


