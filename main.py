import random
import turtle
from turtle import Turtle, Screen

John = Turtle()
turtle.colormode(255)

color_list = [[235, 229, 99], [18, 114, 167], [163, 80, 48], [208, 159, 92], [186, 13, 63], [131, 180, 201], [230, 78, 49], [36, 137, 84], [7, 35, 89], [148, 163, 37], [76, 41, 22], [166, 48, 91], [113, 186, 165], [223, 120, 149], [20, 169, 208], [62, 159, 92], [215, 72, 118], [8, 94, 52], [238, 163, 191], [95, 21, 68], [147, 205, 223], [213, 223, 9], [12, 87, 107], [247, 170, 146], [11, 46, 125], [160, 211, 188]]

John.speed("fastest")


John.setheading(225)
John.penup()
John.hideturtle()
John.fd(300)
John.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    John.fd(50)
    John.dot(20, random.choice(color_list))

    if dot_count % 10 ==0:
        John.setheading(90)
        John.forward(50)
        John.setheading(180)
        John.forward(500)
        John.setheading(0)


screen = Screen()
screen.exitonclick()
