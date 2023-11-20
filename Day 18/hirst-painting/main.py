# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
#
# print(rgb_colors)

import turtle as turtle_module
import random

tim = turtle_module.Turtle()
turtle_module.colormode(255)

color_list = [(225, 233, 227), (207, 160, 82), (54, 89, 130), (145, 91, 40), (140, 26, 49), (222, 206, 108), (132, 177, 203), (45, 55, 103), (158, 46, 83), (169, 159, 39), (129, 189, 143), (83, 20, 44), (38, 43, 67), (186, 94, 107), (186, 140, 170), (85, 120, 180), (59, 39, 31), (88, 157, 92), (78, 153, 164), (195, 79, 73), (161, 201, 219), (79, 74, 44), (45, 74, 77), (57, 126, 123), (220, 183, 167), (218, 176, 188), (167, 206, 166)]
tim.hideturtle()
tim.speed("fastest")
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
tim.pendown()

number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.penup()
    tim.forward(50)
    tim.pendown()

    if dot_count % 10 == 0:
        tim.penup()
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        tim.pendown()
















screen = turtle_module.Screen()
screen.exitonclick()