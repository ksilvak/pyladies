from turtle import forward, left, right, exitonclick, penup, pendown, backward



for i in range(10):
    for x in range(1):
        backward(100)
        left(90)
        forward(100)
        right(90)
        forward(100)
        left(135)
        forward(71)
        left(90)
        forward(71)
        left(90)
        forward(142)
        left(135)
        forward(100)
        left(135)
        forward(142)

    left(135)
    penup()
    forward(100)
    pendown()
    forward(150)



exitonclick()

