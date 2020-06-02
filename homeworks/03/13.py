from turtle import forward, left, right, exitonclick, penup, pendown, backward


for x in range(1):
    penup()
    backward(600)
    pendown()

for dav in range(10):
    ## obličej
    for i in range(1):
        for j in range(18):
            forward(20)
            left(20)
        penup()
        backward(20)
        left(90)
        forward(70)
        left(90)
        pendown()


    ## oči
    for s in range(2):
        for e1 in range(19):
            forward(2)
            right(20)
        penup()
        left(212)
        forward(60)
        pendown()

    ## nos
    for n in range(1):
        penup()
        left(150)
        forward(25)
        pendown()
        right(80)
        forward(20)

    ## ústa
    for m in range(1):
        penup()
        right(45)
        forward(30)
        pendown()
        left(131)
        forward(40)

    penup()
    forward(100)
    pendown()

exitonclick()
