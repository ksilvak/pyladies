from turtle import forward, left, right, exitonclick, penup, pendown, backward


## květ
for  x in range(18):
    for i in range(4):
        forward(60)
        left(90)
    left(20)

right(90)
penup()
forward(60)
pendown()
forward(100)

for z in range(2):
## pravé listy
    left(130)
    forward(40)
    right(10)
    forward(10)
    right(10)
    forward(40)
    right(150)
    forward(40)
    right(10)
    forward(10)
    right(10)
    forward(30)
    right(20)
    forward(5)
    right(20)
    forward(5)
    right(40)
    forward(12)
    left(140)
    forward(50)

## levé listy
    right(130)
    forward(40)
    left(10)
    forward(10)
    left(10)
    forward(40)
    left(150)
    forward(40)
    left(10)
    forward(10)
    left(10)
    forward(30)
    left(20)
    forward(5)
    left(20)
    forward(5)
    left(40)
    forward(12)
    right(140)
    forward(50)

exitonclick()
