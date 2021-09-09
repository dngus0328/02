import turtle

count = 6
while (count > 0):
    turtle.forward(300)
    turtle.penup()
    turtle.left(180)
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.pendown()
    
    count -= 1
    
count = 6
while (count > 0):
    turtle.penup()
    turtle.left(90)
    turtle.forward(360)
    turtle.left(180)
    turtle.pendown()
    turtle.forward(300)
    turtle.penup()
    turtle.left(90)
    turtle.forward(60)
    turtle.right(90)
    turtle.forward(60)
    turtle.left(90)
    turtle.pendown()
    
    count -= 1
    
turtle.exitonclick()


