import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")
#Create the turtle Brad - draws square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(3)
    for i in range(1,16) :
        draw_square(brad)
        brad.right(20)
#Create the turle Amy - draw a circle
#    amy = turtle.Turtle()
#    amy.color("yellow")
#    amy.circle(100)    

    window.exitonclick()

draw_art()
