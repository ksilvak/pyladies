from turtle import forward, left, right, exitonclick, penup, pendown, backward


n = int(input('Zadejte počet úhlů: '))

for i in range(n):
    forward(50)
    left(180 -(180 * (1- 2/n)))

exitonclick()
