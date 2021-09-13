import turtle

def w_turtle():
    turtle.penup()
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(50)
    turtle.stamp()

def a_turtle():
    turtle.penup()
    turtle.setheading(180)
    turtle.pendown()
    turtle.forward(50)
    turtle.stamp()

def s_turtle():
    turtle.penup()
    turtle.setheading(-90)
    turtle.pendown()
    turtle.forward(50)
    turtle.stamp()

def d_turtle():
    turtle.penup()
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.shape('turtle')

turtle.onkey(w_turtle, 'w')
turtle.onkey(a_turtle, 'a')
turtle.onkey(s_turtle, 's')
turtle.onkey(d_turtle, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()
