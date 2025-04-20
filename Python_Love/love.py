import turtle

def draw_heart():
    turtle.bgcolor("black")
    turtle.pensize(3)
    turtle.speed(5)
    turtle.color("red")

    turtle.begin_fill()
    turtle.fillcolor("red")

    # Left side
    turtle.left(50)
    turtle.forward(133)
    turtle.circle(50, 200)
    
    # Right side
    turtle.right(140)
    turtle.circle(50, 200)
    turtle.forward(133)
    
    turtle.end_fill()
    turtle.hideturtle()

# Run function
draw_heart()
turtle.done()
