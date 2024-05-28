def multiply_by_three(user_num):
    print(user_num * 3)

multiply_by_three(8)
multiply_by_three(15)
multiply_by_three(1)
multiply_by_three(3)
multiply_by_three(4)

-------------------------
from turtle import *

speed(50)
width(3)

for i in range(4):
    forward(200)
    left(90)

penup()
goto(0, 300)
pendown()

for i in range(4):
    forward(200)
    left(90)

penup()
goto(-300, 0)
pendown()

for i in range(4):
    forward(200)
    left(90)

penup()
goto(-300,300)
pendown()

for i in range(4):
    forward(200)
    left(90)

exitonclick()